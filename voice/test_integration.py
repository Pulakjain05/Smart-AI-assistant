
from vision_module import get_vision_result
from response_handler import create_response
from command_understanding import understand_command

test_sentences = [
    "What is ahead?",
    "What is on my left?",
    "What is on my right?",
    "What is behind me?",
    "Describe my surroundings",
]

print("TESTING MEMBER 2 INTEGRATION\n")

for sentence in test_sentences:
    print("User:", sentence)

    # Step 1: Convert sentence into a command
    command = understand_command(sentence)
    print("Command:", command)

    # Step 2: Request information from the vision module
    vision_result = get_vision_result(command)
    print("Vision result:", vision_result)

    # Step 3: Convert the result into a spoken response
    response = create_response(vision_result)
    print("Assistant response:", response)

    print("-" * 50)

print("Integration test finished.")