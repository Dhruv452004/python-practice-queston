'''
 Validate Input
Problem: Keep asking the user for input until they enter a number between 1 and 10.

'''



while True:
    number = int(input("Enter a number between 1 and 10: "))
    if(number <= 10):
        print("Shi hai bhai")
        break
    else:
     print("Invalid number, try again")
