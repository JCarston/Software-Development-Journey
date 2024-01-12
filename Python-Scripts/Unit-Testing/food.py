def eat(food, is_healthy):
    ending = "because YOLO!"
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    if is_healthy:
        ending = "because my body is a temple."
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours >=2:
        return f"Ugh I overslepft. I didn't mean to nap so long"
    return f"I'm feeling refreshed after my {num_hours} hour nap"