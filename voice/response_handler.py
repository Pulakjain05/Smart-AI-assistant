
def create_response(vision_result):

    # Handle missing or invalid results
    if not isinstance(vision_result, str) or not vision_result.strip():
        return "Sorry, I couldn't get a clear result."

    result = vision_result.lower().strip()

    if result == "unknown" or result == "none":
        return "Sorry, I couldn't identify the object clearly."

    # Identify the object
    object_name = None

    known_objects = [
        "person", "chair", "door", "vehicle",
        "stairs", "table", "wall", "bicycle"
    ]

    for obj in known_objects:
        if obj in result:
            object_name = obj
            break

    if object_name is None:
        return "Sorry, I couldn't identify the object clearly."

    # Extract distance
    distance = ""

    for word in result.split(","):
        word = word.strip()

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

    if object_name == "stairs":
        subject = "There are stairs"
    else:
        subject = f"There is {article} {object_name}"

    if distance and direction:
        return f"{subject} approximately {distance} {direction}."

    elif distance:
        return f"{subject} approximately {distance} away."

    elif direction:
        return f"{subject} {direction}."

    else:
        return f"{subject} nearby."