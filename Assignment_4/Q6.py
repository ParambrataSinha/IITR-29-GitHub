# Using math module
# a. Write a Python program to convert degrees to radians, and radians to degree.
# b. Write a Python program to calculate the area of a trapezoid.
# c. Write a Python program to calculate the surface volume and area of a cylinder and a sphere.
import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)
def radians_to_degrees(radians):
    return radians * (180 / math.pi)
print("Degrees to Radians:", degrees_to_radians(180))
print("Radians to Degrees:", radians_to_degrees(math.pi))

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height
print("Area of Trapezoid:", trapezoid_area(5, 10, 4))

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height
def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3
def sphere_surface_area(radius):
    return 4 * math.pi * radius**2
print("Cylinder Volume:", cylinder_volume(3, 5))
print("Cylinder Surface Area:", cylinder_surface_area(3, 5))
print("Sphere Volume:", sphere_volume(3))
print("Sphere Surface Area:", sphere_surface_area(3))
