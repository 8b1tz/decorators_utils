import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass    


class Square(Shape):
    def __init__(self, side_length: float):
        self.side_length: float = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

    def calculate_perimeter(self) -> float:
        return 4 * self.side_length


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length: float = length
        self.width: float = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius: float = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, *args):
        if shape_type == "square":
            return Square(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        elif shape_type == "circle":
            return Circle(*args)
        else:
            raise ValueError("Unsupported shape type.")


if __name__ == '__main__':
    square = ShapeFactory.create_shape("square", 5)
    print(square.calculate_area())
    print(square.calculate_perimeter())

    rectangle = ShapeFactory.create_shape("rectangle", 3, 4)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())

    circle = ShapeFactory.create_shape("circle", 3)
    print(circle.calculate_area())
    print(circle.calculate_perimeter())
