
from response_handler import create_response

test_results = [
    "person, 2 metres, ahead",
    "chair, 1 metre, left",
    "door, 2 metres, right",
    "person, 3 metres, behind",
    "unknown",
    ""
]

for result in test_results:
    print("Vision result:", repr(result))

    try:
        response = create_response(result)
        print("Assistant:", response)
    except Exception as error:
        print("ERROR:", error)

    print("-" * 40)