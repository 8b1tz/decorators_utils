class ComplexNumber:
    def __init__(self, real, imaginary) -> None:
        self.__real = real
        self.__imaginary = imaginary

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __str__(self):
        pass
    
    @property
    def get_real(self):
        return self.__real

    @property
    def get_imaginary(self):
        self.__imaginary


if __name__ == "__main__":
    pass
