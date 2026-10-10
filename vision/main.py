import cv2
import time

from vision.detection import ObjectDetector
from vision.utils import get_position


def main():
    detector = ObjectDetector()

    # Stores the last time each object was reported
    last_reported = {}

    # Minimum time before reporting the same object again
    REPORT_INTERVAL = 3

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        success, frame = camera.read()

        if not success:
            print("Error: Could not read frame.")
            break

        frame_height, frame_width = frame.shape[:2]

        # Run YOLO detection on the current frame
        detections = detector.detect(frame)

        for detection in detections:

            # Find object position: left, center, or right
            position = get_position(
                detection["bbox"],
                frame_width
            )

            detection["position"] = position

            # Identify object and position
            object_key = (detection["object"], position)

            # Get current time
            current_time = time.time()

            # Report the object only once every 3 seconds
            if (
                object_key not in last_reported
                or current_time - last_reported[object_key] >= REPORT_INTERVAL
            ):
                print(
                    f"Detected: {detection['object']} | "
                    f"Confidence: {detection['confidence']:.2f} | "
                    f"Position: {position}"
                )

                # Save the reporting time
                last_reported[object_key] = current_time

            # Get bounding box coordinates
            x1, y1, x2, y2 = detection["bbox"]

            # Create object label
            label = f'{detection["object"]} {detection["confidence"]:.2f}'

            # Draw bounding box around detected object
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Display object name and position
            cv2.putText(
                frame,
                f"{label} - {position}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Display the frame AFTER drawing the bounding boxes
        cv2.imshow("AI Assistant - Object Detection", frame)

        # Check for q key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

           
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()