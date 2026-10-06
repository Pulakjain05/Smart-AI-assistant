import cv2
import easyocr

reader = easyocr.Reader(['en'])

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("AI Assistant Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):

        results = reader.readtext(frame)

        texts = []

        for detection in results:

            text = detection[1]
            confidence = detection[2]

            if confidence > 0.5:
                texts.append(text)

        final_text = " ".join(texts)

        print("\nDetected Text:")
        print(final_text)

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()