'''
Question 2:
Ek recursive function likho jo kisi given number ka sum calculate
kare, jo 1 se lekar us number tak ho.

hint 
ye formula use krna   sum = n+sum(n-1)
'''



def sum_of_number(n):
    if(n == 0):
        return  0
    else:
        return n + sum_of_number(n-1)
    
userInput = int(input("enter number: "))
print(f"Sum of numbers from 1 to {userInput} is {sum_of_number(userInput)}")
