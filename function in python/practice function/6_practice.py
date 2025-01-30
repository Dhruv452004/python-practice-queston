'''
Function with Multiple Parameters
Problem: Create a function that takes two numbers as parameters and returns their sum.
'''
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
def sum(num1, num2):
    return num1 + num2
number = sum(num1, num2)
print(f"the sum of {num1} + {num2} is {number}")