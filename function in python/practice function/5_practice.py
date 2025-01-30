'''
Basic Function Syntax
Problem: Write a function to calculate and return the square of a number.
'''
number = int(input("enter number: "))
def square(number):
    return number ** 2 # number * number  yani jese 5 ka square  5 * 5 = 25 
print(f"The square of {number} is {square(number)}")