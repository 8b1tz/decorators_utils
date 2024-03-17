class Equation:
    def __init__(self, coefficient: float, power: float) -> None:
        self.__coefficient = coefficient
        self.__power = power

    def __str__(self) -> str:
        return f"{self.__coefficient}x^{self.__power}"

    @property
    def coefficient(self) -> float:
        return self.__coefficient

    @property
    def power(self) -> float:
        return self.__power

    def evaluate(self, x: float) -> float:
        """
        Avalia a equação para um determinado valor de x.
        """
        return self.__coefficient * (x ** self.__power)

    def derivative(self) -> "Equation":
        """
        Retorna a derivada da equação.
        """
        new_coefficient = self.__coefficient * self.__power
        new_power = self.__power - 1
        return Equation(new_coefficient, new_power)

    def is_equal(self, other: "Equation") -> bool:
        """
        Verifica se duas equações são iguais.
        """
        return self.__coefficient == other.coefficient \
            and self.__power == other.power


if __name__ == '__main__':
    equation = Equation(3, 2)
    print(equation)
    print(equation.coefficient)
    print(equation.power)
    print(equation.evaluate(2))
    derivative = equation.derivative()
    print(derivative)
    print(derivative.evaluate(2))
    equation2 = Equation(3, 2)
    print(equation.is_equal(equation2))
