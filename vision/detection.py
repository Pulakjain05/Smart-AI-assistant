from ultralytics import YOLO

from vision.config import (
    MODEL_PATH,
    DOOR_MODEL_PATH,
    STAIRS_MODEL_PATH,
    CONFIDENCE_THRESHOLD,
    IMAGE_SIZE
)


class ObjectDetector:
    def __init__(self):
        # Load the general YOLO model for common objects
        self.model = YOLO(MODEL_PATH)

        # Load the custom model for doors and handles
        self.door_model = YOLO(DOOR_MODEL_PATH)

        # Load the custom model for stairs
        self.stairs_model = YOLO(STAIRS_MODEL_PATH)

    def detect(self, frame):
        # Run the general YOLO model
        general_results = self.model(
            frame,
            conf=CONFIDENCE_THRESHOLD,
            imgsz=IMAGE_SIZE,
            verbose=False
        )

        # Run the door and handle model
        door_results = self.door_model(
            frame,
            conf=0.60,
            imgsz=IMAGE_SIZE,
            verbose=False
        )

        # Run the stairs model
        stairs_results = self.stairs_model(
            frame,
            conf=0.40,
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

        # Process door and handle detections
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

        # Process stairs detections
        for result in stairs_results:
            for box in result.boxes:
                confidence = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append({
                    "object": "stairs",
                    "confidence": confidence,
                    "bbox": [x1, y1, x2, y2]
                })

        # Find all detected doors
        doors = [
            detection for detection in detections
            if detection["object"] == "door"
        ]

        filtered_detections = []

        # Keep all detections except handles until they are checked
        for detection in detections:
            if detection["object"] != "handle":
                filtered_detections.append(detection)
                continue

            # Find the center of the handle
            handle_x1, handle_y1, handle_x2, handle_y2 = detection["bbox"]
            handle_center_x = (handle_x1 + handle_x2) / 2
            handle_center_y = (handle_y1 + handle_y2) / 2

            handle_is_near_door = False

            # Check whether the handle is inside or near a detected door
            for door in doors:
                door_x1, door_y1, door_x2, door_y2 = door["bbox"]
                margin_x = (door_x2 - door_x1) * 0.15
                margin_y = (door_y2 - door_y1) * 0.15

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

        # Return combined and filtered detections
        return filtered_detections
