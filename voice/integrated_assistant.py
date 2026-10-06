
import speech_recognition as sr
import pyttsx3

from voice.vision_module import get_vision_result
from voice.response_handler import create_response
from voice.command_understanding import understand_command
from voice.text_response_handler import create_text_response
from ocr.ocr_camera import read_text
# -----------------------------
# Text-to-Speech
# -----------------------------
def speak(text):
    print("Assistant:", text)

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as error:
        print("TTS error:", error)


# -----------------------------
# Speech Recognition
# -----------------------------
recognizer = sr.Recognizer()


def listen_for_command():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return None

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None

    except OSError as error:
        print("Microphone problem:", error)
        return None


# -----------------------------
# Main Assistant
# -----------------------------
def main():
    try:
        with sr.Microphone() as source:
            print("Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

    except OSError as error:
        print("Microphone initialization failed:", error)
        return

    speak("AI Vision Assistant is ready.")

    while True:
        text = listen_for_command()

        # Retry if no usable speech was received
        if text is None:
            continue

        command = understand_command(text)
        print("Command:", command)

        # Stop assistant
        if command == "STOP":
            speak("Assistant stopped.")
            break

        # Commands that request information from the vision module
        elif command == "READ_TEXT":

            speak("Please show the text to the camera.")

            ocr_result = read_text()

            if ocr_result:

               print("OCR:", ocr_result)

               response = create_text_response(ocr_result)
               speak(response)

            else:

             speak("Sorry, I could not read the text.")
            
        elif command in [
            "OBJECT_QUERY",
            "LEFT_QUERY",
            "RIGHT_QUERY",
            "BEHIND_QUERY",
            "DESCRIBE_SCENE"
        ]:
            try:
                print("Sending command to Vision Module...")

                result = get_vision_result(command)
                print("Vision:", result)

                response = create_response(result)
                speak(response)

            except Exception as error:
                print("Vision module error:", error)
                speak(
                    "Sorry, I couldn't get information "
                    "from the vision system."
                )

        # Help
        elif command == "HELP":
            speak(
                "You can ask what is ahead, "
                "what is on your left or right, "
                "what is behind you, or ask me "
                "to describe your surroundings. "
                "Say stop to stop the assistant."
            )

        # Unrecognized command
        else:
            speak(
                "Sorry, I didn't understand that command. "
                "Please try again."
            )


if __name__ == "__main__":
    main()