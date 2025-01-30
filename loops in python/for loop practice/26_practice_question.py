'''
Write a program to print multiplication table of number using
for loop in reversed order'''

userInput = int(input("enter number: "))

for number in range(1, 11):
    result = userInput * (11 - number)
    print(f"{userInput} x {11 - number} = {result}")