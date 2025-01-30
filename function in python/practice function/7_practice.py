'''
Polymorphism in Functions
Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
'''


a = int(input("enter number: "))
b = input("enter number and words both: ")

def multiply(a, b):
     # Check if b is a digit (number)
    if b.isdigit():
        return a * int(b) # agr b number hua tho ye use string se int mein convert kr dega
    else:
        return a * b # isme ye number ko string se multiply kr dega jese 5 * p = ppppp 
multiplies = multiply(a, b)
print(f"{a} x {b} is {multiplies}")
