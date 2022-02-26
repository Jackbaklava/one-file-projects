class Matrix:
    def __init__(self, structure, is_adjoint=False):
        self.structure = structure
        self.order = [len(self.structure), len(self.structure[0])]
        # As of right now, the determinant and adjoint can only be calculated of a 2 * 2 matrix
        self.determinant = (
            self.structure[0][0] * self.structure[-1][-1]
            - self.structure[0][-1] * self.structure[-1][0]
        )

        # Could maybe make another class for the adjoint?

        if is_adjoint == False:
            self.adjoint = Matrix(
                [
                    [self.structure[-1][-1], -self.structure[0][-1]],
                    [-self.structure[-1][0], self.structure[0][0]],
                ],
                is_adjoint=True,
            )

    def display_structure(self):
        print("[")
        for row in self.structure:
            row_string = "  ["
            for element in row:
                row_string += str(element)
                if element == row[-1]:
                    row_string += "]"
                else:
                    row_string += ", "

            print(row_string)

        print("]")

    def display_order(self):
        print(f"{self.order[0]} × {self.order[1]}")

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

sample.display_structure()
sample.display_order()
print(sample.determinant)
sample.adjoint.display_structure()
print(sample.adjoint.determinant)
