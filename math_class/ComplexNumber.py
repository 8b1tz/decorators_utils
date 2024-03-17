class ComplexNumber:
    def __init__(self, real, imaginary) -> None:
        self.__real = real
        self.__imaginary = imaginary

    def __add__(self, other):
        real_part = self.__real + other.get_real
        imaginary_part = self.__imaginary + other.get_imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        real_part = self.__real - other.get_real
        imaginary_part = self.__imaginary - other.get_imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.__real * other.get_real - self.__imaginary * \
            other.get_imaginary
        imaginary_part = self.__real * other.get_imaginary + \
            self.__imaginary * other.get_real
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        if self.__imaginary >= 0:
            return f"{self.__real} + {self.__imaginary}i"
        else:
            return f"{self.__real} - {-self.__imaginary}i"

    @property
    def get_real(self):
        return self.__real

    @property
    def get_imaginary(self):
        return self.__imaginary


if __name__ == "__main__":
    complex1 = ComplexNumber(2, 3)
    complex2 = ComplexNumber(1, -2)

    addition = complex1 + complex2
    print("Adição:", addition)

    subtraction = complex1 - complex2
    print("Subtração:", subtraction)

    multiplication = complex1 * complex2
    print("Multiplicação:", multiplication)
