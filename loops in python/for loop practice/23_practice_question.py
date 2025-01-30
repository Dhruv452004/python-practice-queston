'''
Write a program to calculate factorial of a given number using for loop
'''

userInput = int(input("check kro factorial number: "))
factorial = 1


for number in range(1, userInput + 1):
    factorial *= number

print(f"the factorial of {userInput} is: {factorial}")