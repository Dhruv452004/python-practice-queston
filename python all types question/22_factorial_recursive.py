'''

Question 22: "Factorial_Recursive"
Tumhe ek number diya gaya hai num = 5. Tumhe ek recursive function banani hai jo uska factorial calculate kare.

'''

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    elif(n > 1):
        return n * factorial(n-1)
    else:
        return "teri bhes ki tang saale shi number daal le"


num = 5
print(f"factorial of {num} is {factorial(num)}")

