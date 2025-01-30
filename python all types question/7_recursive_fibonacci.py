'''
Question 7: "Recursive_Fibonacci"
Tumhe ek recursive function banani hai jo nth Fibonacci number return kare. Tumhe isme base case aur recursive case ka dhyan rakhna hoga.

isme har number apne pichhle do numbers ka sum hota hai. Jaise:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

forumula 
f(n) = f(n-1) + f(n-2)
'''

def fibonacci(d):
    if (d <=0):
        return "saale kru guddi laal shi number daal"
    
    if(d == 1):
        return 1
    elif(d == 2):
        return 1
    else:
        return fibonacci(d-1) + fibonacci(d-2)

number = int(input("enter number: "))
print(f"The {number}th Fibonacci number is {fibonacci(number)}")