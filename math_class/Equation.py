class Equation:
    def __init__(self, coefficient: float, power: float) -> None:
        self.__coefficient = coefficient
        self.__power = power

    def __str__(self) -> str:
        pass

    @property
    def get_coefficient(self) -> float:
        pass

    @property
    def get_power(self) -> float:
        pass
