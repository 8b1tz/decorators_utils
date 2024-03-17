class Polynomial:
    def __init__(self) -> None:
        self.__coefficients: list = []

    def __str__(self) -> str:
        terms = []
        for degree, coefficient in enumerate(self.__coefficients[::-1]):
            if coefficient != 0:
                if degree == 0:
                    terms.append(str(coefficient))
                elif degree == 1:
                    terms.append(f"{coefficient}x")
                else:
                    terms.append(f"{coefficient}x^{degree}")
        if not terms:
            return "0"
        return " + ".join(terms[::-1])

    def __repr__(self) -> str:
        return f"Polynomial(coefficients={self.__coefficients})"

    def evaluate(self, x: float) -> float:
        result = 0
        for degree, coefficient in enumerate(self.__coefficients):
            result += coefficient * (x ** degree)
        return result

    def differentiate(self) -> 'Polynomial':
        derivative_coefficients = [degree * coef for degree, coef
                                   in enumerate(self.__coefficients)][1:]
        return Polynomial.from_coefficients(derivative_coefficients)

    @staticmethod
    def from_coefficients(coefficients: list) -> 'Polynomial':
        polynomial = Polynomial()
        polynomial.__coefficients = coefficients
        return polynomial


if __name__ == "__main__":
    polynomial = Polynomial.from_coefficients([1, 2, 3])
    print(polynomial)
    result = polynomial.evaluate(2)
    print(result)
    derivative = polynomial.differentiate()
    print(derivative)
