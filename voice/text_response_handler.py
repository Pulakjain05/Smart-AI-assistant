
def create_text_response(ocr_result):
    """Convert OCR output into a response the assistant can speak."""

    if not isinstance(ocr_result, str) or not ocr_result.strip():
        return "Sorry, I couldn't read the text clearly."

    text = ocr_result.strip()

    if text.lower() in ["unknown", "none", "no text detected"]:
        return "Sorry, I couldn't find any readable text."

    return f"The text says: {text}"