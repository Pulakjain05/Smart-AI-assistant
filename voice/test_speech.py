import pyttsx3

engine = pyttsx3.init()

name = "person"
distance = 2

message = f"There is a {name} approximately {distance} metres ahead."

print(message)

engine.say(message)
engine.runAndWait()