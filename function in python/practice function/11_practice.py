'''
Function with *args
Problem: Write a function that takes variable number of arguments and returns their sum.
'''


def calculate_sum(*args):
    return sum(args)
result = calculate_sum(10, 25, 15)
print(f"sum is: {result}")