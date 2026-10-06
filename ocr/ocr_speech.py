import pyttsx3

engine = pyttsx3.init('sapi5')

engine.setProperty('volume', 1.0)
engine.setProperty('rate', 150)

print("Starting speech...")

text=("Hello. i am pulak.")
print("speaking:",text)
engine.say(text)
engine.runAndWait()
print("Speech finished.")


