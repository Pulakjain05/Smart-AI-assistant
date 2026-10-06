
from command_understanding import understand_command
from response_handler import create_response

# Test 1: Command understanding
command_tests = {
    "What is ahead?": "OBJECT_QUERY",
    "What is on my left?": "LEFT_QUERY",
    "What is on my right?": "RIGHT_QUERY",
    "What is behind me?": "BEHIND_QUERY",
    "Describe my surroundings": "DESCRIBE_SCENE",
    "Read this text": "READ_TEXT",
    "Help me": "HELP",
    "Stop listening": "STOP",
        "Please stop": "STOP",
    "Stop this": "STOP",
    "shelf": "UNKNOWN",
    "How is the weather?": "UNKNOWN"
}

print("TESTING COMMAND UNDERSTANDING")

for sentence, expected in command_tests.items():
    actual = understand_command(sentence)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status}: {sentence} -> {actual}")


# Test 2: Response handling
print("\nTESTING RESPONSE HANDLER")

response_tests = [
    ("person, 2 metres, ahead",
     "There is a person approximately 2 metres ahead."),
    ("chair, 1 metre, left",
     "There is a chair approximately 1 metre to your left."),
    ("unknown",
     "Sorry, I couldn't identify the object clearly."),
    ("",
     "Sorry, I couldn't get a clear result."),
]

for vision_result, expected in response_tests:
    actual = create_response(vision_result)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status}: {vision_result!r} -> {actual}")

print("\nTesting finished.")