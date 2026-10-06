
def get_vision_result(command):
    """
    Temporary vision-module interface.

    Replace these simulated results with real vision AI output
    when the vision module is integrated.
    """

    simulated_results = {
        "OBJECT_QUERY": "person, 2 metres, ahead",
        "LEFT_QUERY": "chair, 1 metre, left",
        "RIGHT_QUERY": "door, 2 metres, right",
        "BEHIND_QUERY": "person, 3 metres, behind",
        "DESCRIBE_SCENE": "person, 2 metres, ahead",
    }

    if command == "READ_TEXT":
        return "unknown"  # OCR is handled by the separate OCR module.

    return simulated_results.get(command, "unknown")


if __name__ == "__main__":
    test_commands = [
        "OBJECT_QUERY",
        "LEFT_QUERY",
        "RIGHT_QUERY",
        "BEHIND_QUERY",
        "DESCRIBE_SCENE",
        "INVALID_COMMAND",
    ]

    for command in test_commands:
        print(f"{command} -> {get_vision_result(command)}")