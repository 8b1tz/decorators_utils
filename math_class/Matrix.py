class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__data = [[0] * cols for _ in range(rows)]

    def __str__(self) -> str:
        matrix_str = ""
        for row in self.__data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __repr__(self) -> str:
        return f"Matrix(rows={self.__rows}, cols={self.__cols}, \
            data={self.__data})"

    def __len__(self) -> int:
        return self.__rows

    def __eq__(self, other: 'Matrix') -> bool:
        return self.__rows == other.get_rows and \
            self.__cols == other.get_cols and self.__data == other.get_data

    def __iter__(self):
        self.__iter_index = 0
        return self

    def __next__(self):
        if self.__iter_index < self.__rows:
            result = self.__data[self.__iter_index]
            self.__iter_index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index: int):
        return self.__data[index]

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.__rows != other.get_rows or self.__cols != other.get_cols:
            raise ValueError("Matrizes devem ter as \
                             mesmas dimensões para adição.")
        result = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result[i][j] = self.__data[i][j] + other[i][j]
        return result

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if self.__rows != other.get_rows or self.__cols != other.get_cols:
            raise ValueError("Matrizes devem ter as mesmas \
                             dimensões para subtração.")
        result = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result[i][j] = self.__data[i][j] - other[i][j]
        return result

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.__cols != other.get_rows:
            raise ValueError("Número de colunas da primeira matriz deve ser \
                             igual ao número de linhas da segunda matriz.")
        result = Matrix(self.__rows, other.get_cols)
        for i in range(self.__rows):
            for j in range(other.get_cols):
                for k in range(self.__cols):
                    result[i][j] += self.__data[i][k] * other[k][j]
        return result

    @property
    def get_rows(self) -> int:
        return self.__rows

    @property
    def get_cols(self) -> int:
        return self.__cols

    @property
    def get_data(self) -> list:
        return self.__data

    def transpose(self) -> 'Matrix':
        transposed = Matrix(self.__cols, self.__rows)
        for i in range(self.__rows):
            for j in range(self.__cols):
                transposed[j][i] = self.__data[i][j]
        return transposed


if __name__ == "__main__":
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(3, 2)
    print(matrix1)
    print(len(matrix1))
    print(matrix1.get_rows)
    print(matrix1.get_cols)
    print(matrix1.get_data)
    matrix1[0][1] = 2
    print(matrix1)
    print(matrix1 + matrix2)
    matrix2[0][0] = 1
    matrix2[1][1] = 2
    matrix2[2][0] = 3
    matrix2[2][1] = 4
    print(matrix2)
