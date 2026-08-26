'''Write OOP classes to handle the following scenarios:
A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line

'''

class Point:

    #create coordinates
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    #print coordinates
    def __str__(self):
        return '({},{})'.format(self.x_cod,self.y_cod)

    #distance method
    def distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5

    #distance from origin 
    def distance_origin(self):
        return ((self.x_cod)**2+(self.y_cod)**2)**0.5
    

class Line:
    #line create
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    #line display
    def __str__(self):
        return '{}x+{}y+{}=0'.format(self.A,self.B,self.C)

    #check if point on line
    def check_point(line,point):
        if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
            return True
        else:
            return False

    #distance between point and line
    def distance_from_point(line,point):
        return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5

    
p1=Point(1,2)
print(p1)
p2=Point(3,4)
print(p2)

print(p1.distance(p2))

print(p1.distance_origin())

l1=Line(2,3,4)
print(l1)

print(l1.check_point(p1))
print(l1.distance_from_point(p1))