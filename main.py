# Base

class Vector:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y

    def __repr__(self):
        return f"The vector is <{self.xcoord},{self.ycoord}>"


class ThDVector(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.zcoord = z

    def __repr__(self):
        return f"The vector is <{self.xcoord},{self.ycoord},{self.zcoord}>"


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
    print(v1)
    
    v2 = ThDVector(1,2,3)
    print(v2)
