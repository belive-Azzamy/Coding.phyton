import math

def area_of_square(side):
    area = side * side
    text = f"Area of Square with {side} is {area}"
    print(text)

def area_of_triangle(height, base):
    area = 0.5 * height * base
    text = f"Area of Triangle with {height} and {base} is {area}"
    print(text)

def area_of_circle(r):
    area = math.pi * r * r
    text = f"Area of Circle with Radius {r} is {area}"
    print(text)