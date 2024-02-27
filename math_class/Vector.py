from math import sqrt


class Vector3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self) -> str:
        return f'X: {self.__x}, Y: {self.__y}, Z: {self.__z}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__x}, {self.__y}, {self.__z})"

    def __len__(self) -> int:
        return sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.__x + other.__x, self.__y + other.__y,
                        self.__z + other.__z)

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.__x - other.__x, self.__y - other.__y,
                        self.__z - other.__z)

    def __iter__(self):
        yield self.__x
        yield self.__y
        yield self.__z

    def __mul__(self, scalar: float) -> 'Vector3D':
        return Vector3D(self.__x * scalar, self.__y * scalar,
                        self.__z * scalar)

    def dot_product(self, other: 'Vector3D') -> float:
        return self.__x * other.__x + self.__y * other.__y + self.__z * \
            other.__z

    def cross_product(self, other: 'Vector3D') -> 'Vector3D':
        cross_x = self.__y * other.__z - self.__z * other.__y
        cross_y = self.__z * other.__x - self.__x * other.__z
        cross_z = self.__x * other.__y - self.__y * other.__x
        return Vector3D(cross_x, cross_y, cross_z)


if __name__ == "__main__":
    vector1 = Vector3D(2, 3, 1)
    vector2 = Vector3D(1, -1, 2)
    print(vector1 + vector2)
    print(vector1 - vector2)
    print(vector1 * 2.0)
    print(vector2 * 5.0)
    print(vector1.dot_product(vector2))
    print(vector1.cross_product(vector2))
