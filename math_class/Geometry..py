class Geometry:
    def __init__(self, shape: str) -> None:
        self.__shape = shape
        self.__dimensions = []

    def __str__(self) -> str:
        pass

    def get_shape(self) -> float:
        pass

    def get_dimensions(self) -> list:
        pass

    def calculate_area(self) -> float:
        pass

    def calculate_perimeter(self) -> float:
        pass
    
    def add_dimension(self, dimension: float):
        self.__dimensions.append(dimension)
