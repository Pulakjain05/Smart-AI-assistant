import cv2

from detection import ObjectDetector
from utils import get_position


class VisionInterface:
    def __init__(self):
        self.detector = ObjectDetector()
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise RuntimeError("Could not open camera.")

    def get_result(self, command):
        """
        Capture one camera frame and return the most relevant
        detection for the voice command.
        """

        success, frame = self.camera.read()

        if not success:
            return "unknown"

        frame_height, frame_width = frame.shape[:2]

        detections = self.detector.detect(frame)

        if not detections:
            return "unknown"

        # Add position to every detection
        for detection in detections:
            detection["position"] = get_position(
                detection["bbox"],
                frame_width
            )

        # Decide which detections are relevant
        if command == "LEFT_QUERY":
            relevant = [
                d for d in detections
                if d["position"] == "left"
            ]

        elif command == "RIGHT_QUERY":
            relevant = [
                d for d in detections
                if d["position"] == "right"
            ]

        elif command == "BEHIND_QUERY":
            # Vision currently cannot detect behind the user.
            return "unknown"

        elif command in [
            "OBJECT_QUERY",
            "DESCRIBE_SCENE"
        ]:
            relevant = detections

        else:
            return "unknown"

        if not relevant:
            return "unknown"

        # Choose the highest-confidence detection
        best_detection = max(
            relevant,
            key=lambda d: d["confidence"]
        )

        object_name = best_detection["object"]
        position = best_detection["position"]

        # Convert vision position into the language
        # expected by Member 2's response handler.
        if position == "center":
            direction = "ahead"
        elif position == "left":
            direction = "left"
        elif position == "right":
            direction = "right"
        else:
            direction = ""

        if direction:
            return f"{object_name}, {direction}"

        return object_name

    def close(self):
        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    vision = VisionInterface()

    try:
        while True:

            result = vision.get_result("OBJECT_QUERY")

            print("Vision result:", result)

            key = input("Press Enter for another detection or type q to quit: ")

            if key.lower() == "q":
                break

    finally:
        vision.close()