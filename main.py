class TwoDimensionalVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.x}, {self.y}>"

    def scalar_multiply(self, scalar):
        return TwoDimensionalVector(self.x * scalar, self.y * scalar)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y


class ThreeDimensionalVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def scalar_multiply(self, scalar):
        return ThreeDimensionalVector(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


class VectorFuncs:
    @staticmethod
    def dot_product(v1, v2):
        return v1.dot_product(v2)

    @staticmethod
    def thd_dot_product(v1, v2):
        return v1.dot_product(v2)


if __name__ == '__main__':
    v1 = TwoDimensionalVector(1, 2)
    print(v1.scalar_multiply(3))
    print(VectorFuncs.dot_product(v1, TwoDimensionalVector(2, 3)))

    v2 = ThreeDimensionalVector(1, 2, 3)
    print(v2.scalar_multiply(3))
    print(VectorFuncs.thd_dot_product(v2, ThreeDimensionalVector(2, 3, 4)))
