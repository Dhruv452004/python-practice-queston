'''
Write a program to find whether a given number is prime or not
'''

userInput = int(input("jis number ka table chaiye vo number daal: "))

# is_prime = True
for number in range(2, userInput):
    if (userInput % number) == 0:
        print(f"{userInput} is not Prime")
        break
    
else:
    print(f"{userInput} is Prime")
    

