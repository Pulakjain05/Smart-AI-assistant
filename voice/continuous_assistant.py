import speech_recognition as sr
import pyttsx3


# -----------------------------
# Text-to-Speech
# -----------------------------
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Understand Command
# -----------------------------
def understand_command(text):
    text = text.lower()

    if "what is ahead" in text or "what is in front" in text:
        return "OBJECT_QUERY"

    elif "read this" in text or "read the text" in text:
        return "READ_TEXT"

    elif "describe" in text or "surroundings" in text:
        return "DESCRIBE_SCENE"

    elif "help" in text:
        return "HELP"

    elif "stop" in text:
        return "STOP"

    else:
        return "UNKNOWN"


# -----------------------------
# Speech Recognition
# -----------------------------
recognizer = sr.Recognizer()


# Reduce background noise
with sr.Microphone() as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

speak("Voice assistant is ready.")


# -----------------------------
# Continuous Listening
# -----------------------------
while True:

    try:
        with sr.Microphone() as source:

            print("\n🎤 Listening...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        command = understand_command(text)

        print("Command:", command)


        # -----------------------------
        # Responses
        # -----------------------------

        if command == "OBJECT_QUERY":

            speak("I will check what is ahead.")

        elif command == "READ_TEXT":

            speak("I will read the text.")

        elif command == "DESCRIBE_SCENE":

            speak("I will describe your surroundings.")

        elif command == "HELP":

            speak("How can I help you?")

        elif command == "STOP":

            speak("Voice assistant stopped.")
            break

        else:

            speak("Sorry, I did not understand the command.")


    except sr.UnknownValueError:

        print("Could not understand.")

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")
        break