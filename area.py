import math

def area_circle(r):
    return math.pi *r * r

def area_square(side):
    return side*side

def area_triangle(base,height):
    return 0.5 * base * height

def area_rectangle(b,l):
    return b*l

r = int(input("Enter radius of circle: "))
side = int(input("Enter side of square: "))
base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

print("Area of the circle is: ",area_circle(r) )
print("Area of the square is: ",area_square(side))
print("Area of the triangle is : ",area_triangle(base,height))
print("Area of the rectangle is :",area_rectangle(b,l) )
