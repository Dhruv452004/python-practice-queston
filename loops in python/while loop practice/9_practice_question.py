'''
Write a program to find the sum first natural numbers using while loop
'''


userInput = int(input("check natural number: "))
nunmber = 1
sum = 0

while(nunmber <= userInput):
    sum += nunmber
    nunmber += 1

print("Sum of first", userInput, "natural numbers is:", sum)

