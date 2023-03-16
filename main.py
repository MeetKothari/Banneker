# Base

class Vector:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y

    def __repr__(self):
        return f"The vector is <{self.xcoord},{self.ycoord}>"
    
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("The built-in multiplier only allows scalar/vector multiplication. If you're looking for dotproduct or crossproduct, please refer to the 'funcs' class.")
        self.xcoord = self.xcoord * x
        self.ycoord = self.ycoord * x
        return f"<{self.xcoord}, {self.ycoord}>"
    def __add__(self, other):
        x = self.xcoord + other.xcoord
        y = self.ycoord + other.ycoord
        return Vector(x, y)
    
    def __sub__(self, other):
        x = self.xcoord - other.xcoord
        y = self.ycoord - other.ycoord
        return Vector(x, y)

    def __truediv__(self, scalar):
        x = self.xcoord / scalar
        y = self.ycoord / scalar
        return Vector(x, y)

    def magnitude(self):
        return math.sqrt(self.xcoord ** 2 + self.ycoord ** 2)

    def normalize(self):
        mag = self.magnitude()
        x = self.xcoord / mag
        y = self.ycoord / mag
        return Vector(x, y)

    def dot_product(self, other):
        return self.xcoord * other.xcoord + self.ycoord * other.ycoord
    
    def angle_between(self, other, degrees=True):
        dot_product = self.dot_product(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()
        cos_angle = dot_product / (mag1 * mag2)
        angle = math.acos(cos_angle)
        if degrees:
            return math.degrees(angle)
        else:
            return angle

    def projection(self, other):
        dot_product = self.dot_product(other)
        mag2 = other.magnitude()
        scalar_proj = dot_product / mag2
        unit_vec = other.normalize()
        return unit_vec * scalar_proj


class ThDVector(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.zcoord = z

    def __repr__(self):
        return f"The vector is <{self.xcoord},{self.ycoord},{self.zcoord}>"
    
    def __mul__(self, x):
        super().__mul__(x)
        self.zcoord = self.zcoord * x
        return f"<{self.xcoord}, {self.ycoord}, {self.zcoord}>"


class funcs:
    def dotproduct(v1, v2):
        xcoord = v1.xcoord * v2.xcoord
        ycoord = v1.ycoord * v2.ycoord
        scalar = xcoord + ycoord
        print("The scalar resulting from the Dot Product of the given vectors is: " + str(scalar))

    def thddotproduct(v1: ThDVector, v2: ThDVector):
        xcoord = v1.xcoord * v2.xcoord
        ycoord = v1.ycoord * v2.ycoord
        zcoord = v1.zcoord * v2.zcoord
        scalar = xcoord + ycoord + zcoord
        print("The scalar resulting from the Dot Product of the given vectors is: " + str(scalar))


if __name__ == '__main__':
    v1 = Vector(1, 2)
    print(v1*3)
    
    v2 = ThDVector(1,2,3)
    print(v2*3)
