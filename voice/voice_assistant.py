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
# Speech-to-Text
# -----------------------------
recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("🎤 Speak a command...")
    audio = recognizer.listen(source)


try:
    text = recognizer.recognize_google(audio)

    print("You said:", text)

    command = understand_command(text)

    print("Command:", command)


    # -----------------------------
    # Assistant Response
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
        speak("Stopping.")

    else:
        speak("Sorry, I did not understand the command.")


except sr.UnknownValueError:
    speak("Sorry, I could not understand your voice.")

except sr.RequestError:
    speak("Speech recognition service is unavailable.")