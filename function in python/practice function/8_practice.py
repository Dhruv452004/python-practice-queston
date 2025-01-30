'''
Function Returning Multiple Values
Problem: Create a function that returns both the area and circumference of a circle given its radius.


Area of a circle: formula
π x radius ka square  yani radius**

circumference: formula
2 x π x radius

math.pi yani π jiski value 3.14 hoti h
''' 

import math # taki hume pi ( π ) ki value mil jaye

radius = int(input("ente number: "))

def circle(radius):
    # area of a cricle 
    area_of_a_cricle =  math.pi * radius ** 2

    # cricumference of a circle 
    circumference_of_a_cricle = 2 * math.pi * radius

    # Round to 2 decimal places (example = 1.33333 after use round 1.33)
    area_of_a_cricle = round(area_of_a_cricle, 2)
    circumference_of_a_cricle = round(circumference_of_a_cricle, 2)

    return area_of_a_cricle, circumference_of_a_cricle

result = circle(radius)
print(f"area of a circle is {result[0]}")
print(f"circumference of a circle is {result[1]}") 