class Matrix:
    def __init__(self, structure):
        self.structure = structure
        self.order = f"{len(self.structure)} × {len(self.structure[0])}"
        self.determinant = "smh"
        self.adjoint = "smh"

    def display(self):
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


sample = Matrix(
    [
        [1, 2],
        [3, 4],
    ]
)
# Same thing as [ [1, 2], [3, 4] ]

sample.display()
print(sample.order)
