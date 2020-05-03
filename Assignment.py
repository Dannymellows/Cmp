"""

This is to calculate the area of a square
Name:Ndubueze Daniella Onyinyechi
Dept:Computer Science
Level: 100
Matric number: BHU/19/04/05/0064
"""
from typing import Any, Union


def square():
    a = int(input("Enter the area :"))
    result = a**2
    print(result)
square()

"""

This is to calculate the area of a rectangle

"""
def rectangle():
    l = int(input("Please enter your length: "))
    b = int(input("Please enter your breadth: "))
    result = l* b
    print (result)
rectangle()


"""

This is to calculate the area of a triangle

"""
def triangle():
    b =int(input("Please enter base: "))
    h =int(input("Please enter height :"))
    result = b * h/2
    print(result)
triangle()

"""
This is to calculate area of a trapezoid 

"""
def trapezoid():
    b= int(input(" Enter your base: "))
    b2= int(input("Enter the second base: "))
    h = int(input ("Enter your height: "))
    result = b + b2 * h/ 2
    print(result)
trapezoid()

"""
This is to calculate the area of a circle

"""
def circle():
    r= int(input("Enter the radius: "))
    import math
    x= math.pi
    result = r**2 * x
    print (result)
circle()

"""
This is to calculate surface area of a cube

"""
def cube():
    S = 6
    a= int(input("the length of the side of the cube: "))
    result = S * a**2
    print(result)
cube()

"""
This is to calculate the curved surface area of the cirle

"""
def curved_surface():
    r = int(input("Enter Radius:"))
    height = int(input(" Enter height:"))
    import math
    x = math.pi
    print(2*r*height*x)
curved_surface()
"""
This is to calculate the total surface area of a cylinder

"""
def total_surface():
    r = int(input("Enter radius: "))
    h = int(input("Enter height: "))
    import math
    x= math.pi
    result = 2*x*r *(r + h)
    print(result)
total_surface()

"""
This is to calculate the volume of the cylinder
"""
def Volume():
    r=int(input("Enter the radius: "))
    h=int(input("Enter the height: "))
    import math
    x = math.pi
    Result = x* r**2 *h
    print(Result)
Volume()

"""
This is to calculate the acceleration formula
"""
def Acceleration():
    v=int(input("Enter final velocity: "))
    u=int(input("Enter initial velocity: "))
    t=int(input("Enter time: "))
    a = (v -u)/t
    print (a)
Acceleration()

"""
This is to calculate density
"""
def density():
    m= int(input("Enter mass: "))
    v= int(input("Enter volume: "))
    p= m/v
    print(p)
density()

"""
This is to calculate pressure
"""
def pressure():
    f= int(input("Enter force: "))
    A= int(input("Enter a: "))
    p=f/A
    print(p)
pressure()

"""
This is to calculate kinetic energy
"""
def kinetic_energy():
    m =int(input("enter mass: "))
    v =int(input("enter velocity: "))
    kinetic = m*v**2/ 2
    print(kinetic)
kinetic_energy()

"""
This is to calculate voltage
"""
def voltage():
    I = int(input("enter current: "))
    R =int(input("Enter resistance: "))
    v= I* R
    print(v)

voltage()