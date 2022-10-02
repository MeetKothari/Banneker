# Base 

class Vector:
    def __init__(self,x,y):
        self.xcoord = x
        self.ycoord = y 
    
    def print(self):
        print("The vector is: " + "<" + str(self.xcoord) + "," + str(self.ycoord) + ">")
        
        
class ThDVector(Vector):
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.zcoord = z
    
    def print(self):
        print("The vector is: " + "<" + str(self.xcoord) + "," + str(self.ycoord) + "," + str(self.zcoord) + ">")

class funcs:
    def dotproduct(v1,v2):
        xcoord = v1.xcoord * v2.xcoord
        ycoord = v1.ycoord * v2.ycoord
        scalar = xcoord + ycoord
        print("The scalar resulting from the Dot Product of the given vectors is: " + str(scalar))
    



if __name__ == '__main__':
    v1 = Vector(1,2)
    v1.print()
    
    v2 = Vector(4,5)
    v2.print()
    
    funcs.dotproduct(v1, v2)
    
    v4 = ThDVector(1,2,3)
    v4.print()
