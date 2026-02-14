class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("side_a must be greater than 0")
            super().__setattr__(key, value)

        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("angle_a must be between 0 and 180")
            super().__setattr__("angle_a", value)
            super().__setattr__("angle_b", 180 - value)

        elif key == "angle_b":
            if not (0 < value < 180):
                raise ValueError("angle_b must be between 0 and 180")
            super().__setattr__("angle_b", value)
            super().__setattr__("angle_a", 180 - value)

        else:
            super().__setattr__(key, value)


rhombus = Rhombus(10, 60)
print(f"Сторона a: {rhombus.side_a}")
print(f"Кут a: {rhombus.angle_a}")
print(f"Кут b: {rhombus.angle_b}")

rhombus.angle_a = 30
print(f"Новий кут b: {rhombus.angle_b}")
