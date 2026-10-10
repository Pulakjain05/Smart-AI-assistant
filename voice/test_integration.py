

from voice.command_understanding import understand_command
from voice.response_handler import create_response
from vision.vision_interface import VisionInterface

test_sentences = [
    "What is ahead?",
    "What is on my left?",
    "What is on my right?",
    "What is behind me?",
    "Describe my surroundings",
]

print("TESTING MEMBER 2 INTEGRATION\n")

vision = VisionInterface()

try:
    for sentence in test_sentences:
        print("User:", sentence)

        # Step 1: Convert the sentence into a command
        command = understand_command(sentence)
        print("Command:", command)

        # Step 2: Request information from the vision module
        vision_result = vision.get_result(command)
        print("Vision result:", vision_result)

        # Step 3: Convert the result into a response
        response = create_response(vision_result)
        print("Assistant response:", response)

        print("-" * 50)

    print("Integration test finished.")

finally:
    vision.close()
