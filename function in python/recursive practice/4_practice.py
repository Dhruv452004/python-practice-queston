'''
Recursive Function
Problem: Create a recursive function to calculate the factorial of a number.
'''

def calculate_factorial_number(number):
    if(number == 0 or number == 1):
        return 1
    else:
        return number * calculate_factorial_number(number - 1)
    
number = int(input("enter number: "))
result = (calculate_factorial_number(number))
print(f"Factorial of {number} is {result}")