

def create_response(vision_result):

    # Handle missing or invalid results
    if not isinstance(vision_result, str) or not vision_result.strip():
        return "Sorry, I couldn't get a clear result."

    result = vision_result.lower().strip()

    # Handle unknown results
    if result in ["unknown", "none"]:
        return "Sorry, I couldn't identify the object clearly."

    # Split the result
    parts = [part.strip() for part in result.split(",")]

    # First part is normally the object name
    object_name = parts[0]

    if not object_name:
        return "Sorry, I couldn't identify the object clearly."

    # Extract distance
    distance = ""

    for word in parts:
        if "metre" in word or "meter" in word:
            distance = word
            break

    # Identify direction
    if "left" in result:
        direction = "to your left"
    elif "right" in result:
        direction = "to your right"
    elif "behind" in result:
        direction = "behind you"
    elif "ahead" in result or "front" in result:
        direction = "ahead"
    else:
        direction = ""

    # Build natural spoken response
    article = "an" if object_name[0] in "aeiou" else "a"

    # Special plural objects
    if object_name in ["stairs", "people"]:
        subject = f"There are {object_name}"
    else:
        subject = f"There is {article} {object_name}"

    # Add distance and direction
    if distance and direction:
        return f"{subject} approximately {distance} {direction}."

    elif distance:
        return f"{subject} approximately {distance} away."

    elif direction:
        return f"{subject} {direction}."

    else:
        return f"{subject} nearby."
