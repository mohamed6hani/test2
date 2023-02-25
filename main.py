
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"Point C ({self.x + other.x}, {self.y + other.y})"

    def print(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(4, 2)
other = Point(1, 3)
print(point + other)
