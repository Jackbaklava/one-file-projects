class Matrix:
    def __init__(self, structure):
        self.structure = structure
        self.order = [len(self.structure), len(self.structure[0])]
        self.order_string = f"{self.order[0]} × {self.order[1]}"

    def __str__(self):
        matrix_string = "["

        for row in self.structure:
            matrix_string += "\n" + "  ["

            for element in row:
                matrix_string += str(element)
                if element == row[-1]:
                    matrix_string += "]"
                else:
                    matrix_string += ", "

        matrix_string += "\n" + "]"

        return matrix_string

    def adjoint(self):
        return Matrix(
            [
                [self.structure[-1][-1], -self.structure[0][-1]],
                [-self.structure[-1][0], self.structure[0][0]],
            ]
        )

    def determinant(self):
        return (
            self.structure[0][0] * self.structure[-1][-1]
            - self.structure[0][-1] * self.structure[-1][0]
        )

    def is_equal_to(self):
        pass

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        # could be by scalar or matrix
        pass

    def inverse(self):
        pass


sample = Matrix([[1, 2], [3, 4]])
# Same thing as [ [1, 2], [3, 4] ]

print(sample)
print(sample.order_string)
print(sample.determinant())
