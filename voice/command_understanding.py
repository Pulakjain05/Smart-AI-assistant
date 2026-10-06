
def understand_command(text):
    """Convert a spoken sentence into a recognized command."""

    if not text or not text.strip():
        return "UNKNOWN"

    text = text.lower().strip()

    # Remove common punctuation
    for mark in ["?", ".", ",", "!"]:
        text = text.replace(mark, "")

    # Left direction
    if any(phrase in text for phrase in [
        "on my left",
        "to my left",
        "left side",
        "on the left",
        "to the left"
    ]):
        return "LEFT_QUERY"

    # Right direction
    elif any(phrase in text for phrase in [
        "on my right",
        "to my right",
        "right side",
        "on the right",
        "to the right"
    ]):
        return "RIGHT_QUERY"

    # Behind
    elif any(phrase in text for phrase in [
        "behind me",
        "what is behind",
        "what's behind",
        "at my back"
    ]):
        return "BEHIND_QUERY"

    # Front / ahead

    # Front / ahead
    elif any(phrase in text for phrase in [
        "what is ahead",
        "what's ahead",
        "what is the head",
"what's the head",
"what is a head",
"what's a head",
        "what is in ahead",
        "what is in front of me",
        "in front of me",
        "in front",
        "ahead of me",
        "in my way"
    ]):
        return "OBJECT_QUERY"

    # Read text
    elif any(phrase in text for phrase in [
        "read",
        "read this",
        "read the text",
        "read this text",
        "read it aloud"
    ]):
        return "READ_TEXT"

    # Scene description
    elif any(phrase in text for phrase in [
        "describe my surroundings",
        "describe the surroundings",
        "describe my environment",
        "what is around me",
        "what's around me",
        "describe the scene"
    ]):
        return "DESCRIBE_SCENE"

    # Help

    # Help: match complete words and common phrases
    elif any(phrase in text.split() for phrase in ["help", "emergency"]):
        return "HELP"

    # Stop: match supported stop commands
    elif text in [
        "stop",
        "stop this",
        "please stop",
        "please stop listening",
        "stop listening",
        "shut down",
        "exit assistant",
        "quit assistant"
    ]:
        return "STOP"

    return "UNKNOWN"


if __name__ == "__main__":
    test_commands = [
        "What is ahead?",
        "Can you tell me what's on my left?",
        "Please tell me what is on my right",
        "What is behind me?",
        "Could you describe my surroundings?",
        "Read this text",
        "Help me",
        "Stop listening",
        "Stop this",
        "Please stop listening",
        "How is the weather?"
    ]

    for sentence in test_commands:
        command = understand_command(sentence)
        print(f"{sentence} -> {command}")
