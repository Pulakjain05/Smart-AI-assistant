
from text_response_handler import create_text_response

tests = [
    ("Welcome", "The text says: Welcome"),
    ("EXIT", "The text says: EXIT"),
    ("", "Sorry, I couldn't read the text clearly."),
    ("unknown", "Sorry, I couldn't find any readable text."),
]

for text, expected in tests:
    actual = create_text_response(text)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status}: {text!r} -> {actual}")