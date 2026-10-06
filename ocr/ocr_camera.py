import cv2
import easyocr


# Create OCR reader once
reader = easyocr.Reader(['en'])


def read_text():
    """
    Opens the camera and reads text when the user presses R.
    Returns the detected text as a string.
    """

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("OCR: Could not open camera.")
        return ""

    try:

        print("OCR: Camera started.")
        print("Press R to read text.")
        print("Press Q to cancel.")

        while True:

            ret, frame = camera.read()

            if not ret:
                print("OCR: Could not read camera frame.")
                return ""

            cv2.imshow(
                "OCR - Press R to Read / Q to Cancel",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            # Read text
            if key == ord('r'):

                print("OCR: Reading text...")

                results = reader.readtext(frame)

                texts = []

                for detection in results:

                    text = detection[1]
                    confidence = detection[2]

                    if confidence > 0.5:
                        texts.append(text)

                final_text = " ".join(texts).strip()

                return final_text

            # Cancel
            elif key == ord('q'):

                print("OCR: Cancelled.")
                return ""

    finally:

        camera.release()
        cv2.destroyAllWindows()


# -----------------------------
# TEST
# -----------------------------

if __name__ == "__main__":

    result = read_text()

    if result:
        print("\nDetected Text:")
        print(result)

    else:
        print("\nNo text detected.")