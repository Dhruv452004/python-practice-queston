'''
 Write a program to print multiplication table of a
 given number using for loop
 '''


userInput = int(input("jis number ka table chaiye vo number daal: "))

for number in range(1, 11):
    result = userInput * number
    print(f"{userInput} x {number} = {result}")