from .Shape import ShapeFactory


class Geometry:
    def __init__(self, shape: str) -> None:
        self.__shape = shape
        self.__dimensions = []

    def __str__(self) -> str:
        return f"Shape: {self.__shape}, Dimensions: {self.__dimensions}"

    def get_shape(self) -> str:
        return self.__shape

    def get_dimensions(self) -> list:
        return self.__dimensions

    def calculate_area(self) -> float:
        shape_instance = ShapeFactory.create_shape(self.__shape,
                                                   *self.__dimensions)
        return shape_instance.calculate_area()

    def calculate_perimeter(self) -> float:
        shape_instance = ShapeFactory.create_shape(self.__shape,
                                                   *self.__dimensions)
        return shape_instance.calculate_perimeter()

    def add_dimension(self, dimension: float):
        self.__dimensions.append(dimension)


if __name__ == '__main__':
    geometry = Geometry("square")
    geometry.add_dimension(5)
    print(geometry.calculate_area())
    print(geometry.calculate_perimeter())
