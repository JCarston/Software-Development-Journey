def eat(food, is_healthy):
    ending = "because YOLO!"
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    if is_healthy:
        ending = "because my body is a temple."
    return f"I'm eating {food}, {ending}"