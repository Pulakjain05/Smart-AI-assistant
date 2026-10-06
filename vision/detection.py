from ultralytics import YOLO

from config import (
    MODEL_PATH,
    DOOR_MODEL_PATH,
    CONFIDENCE_THRESHOLD,
    IMAGE_SIZE
)


class ObjectDetector:
    def __init__(self):
        # Load the general YOLO model for common objects
        self.model = YOLO(MODEL_PATH)

        # Load the custom model for doors and handles
        self.door_model = YOLO(DOOR_MODEL_PATH)

    def detect(self, frame):

        # Run the general YOLO model
        general_results = self.model(
            frame,
            conf=CONFIDENCE_THRESHOLD,
            imgsz=IMAGE_SIZE,
            verbose=False
        )

        # Run the custom door/handle model
        # A slightly higher threshold helps reduce false handle detections
        door_results = self.door_model(
            frame,
            conf=0.60,
            imgsz=IMAGE_SIZE,
            verbose=False
        )

        detections = []

        # Process general YOLO detections
        for result in general_results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                object_name = self.model.names[class_id]

                detections.append({
                    "object": object_name,
                    "confidence": confidence,
                    "bbox": [x1, y1, x2, y2]
                })

        # Process custom door/handle detections
        for result in door_results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                object_name = self.door_model.names[class_id]

                detections.append({
                    "object": object_name,
                    "confidence": confidence,
                    "bbox": [x1, y1, x2, y2]
                })

        # Find all detected doors
        doors = [
            detection for detection in detections
            if detection["object"] == "door"
        ]

        filtered_detections = []

        # Check every detection
        for detection in detections:

            # Keep everything except handles
            if detection["object"] != "handle":
                filtered_detections.append(detection)
                continue

            # Get handle bounding box
            handle_x1, handle_y1, handle_x2, handle_y2 = detection["bbox"]

            # Find center point of the handle
            handle_center_x = (handle_x1 + handle_x2) / 2
            handle_center_y = (handle_y1 + handle_y2) / 2

            handle_is_near_door = False

            # Compare the handle with every detected door
            for door in doors:

                # Get door bounding box
                door_x1, door_y1, door_x2, door_y2 = door["bbox"]

                # Slightly expand the door area
                # This allows handles near the door boundary
                margin_x = (door_x2 - door_x1) * 0.15
                margin_y = (door_y2 - door_y1) * 0.15

                # Check whether the handle is inside or near the door
                if (
                    door_x1 - margin_x <= handle_center_x <= door_x2 + margin_x
                    and
                    door_y1 - margin_y <= handle_center_y <= door_y2 + margin_y
                ):
                    handle_is_near_door = True
                    break

            # Keep the handle only when it is associated with a door
            if handle_is_near_door:
                filtered_detections.append(detection)

        # Return the final filtered detections
        return filtered_detections