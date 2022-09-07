# Base 

class Vector:
    def __init__(self,x,y):
        self.xcoord = x
        self.ycoord = y 
    def print(self):
        print("The vector is: " + "<" + str(self.xcoord) + "," + str(self.ycoord) + ">")



if __name__ == '__main__':
    v1 = Vector(1,2)
    v1.print()
    
    
