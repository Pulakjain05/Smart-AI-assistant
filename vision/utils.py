def get_position(bbox, frame_width):
    """
    Determine whether an object is on the left,
    center, or right side of the frame.
    """

    x1, y1, x2, y2 = bbox

    # Find the center of the detected object
    object_center_x = (x1 + x2) / 2

    # Divide the frame into three regions
    left_boundary = frame_width * 0.33
    right_boundary = frame_width * 0.66

    if object_center_x < left_boundary:
        return "left"

    elif object_center_x > right_boundary:
        return "right"

    else:
        return "center"