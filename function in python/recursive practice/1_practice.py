'''
Question 1:
Ek recursive function likho jo kisi number ka factorial calculate kare.

Recursive case:
factorial(n)=n*factorial(n-1)

Base case:
factorial(0)=1'''

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("enter number: "))
print(f"factorial of {n} is {factorial(n)}")

