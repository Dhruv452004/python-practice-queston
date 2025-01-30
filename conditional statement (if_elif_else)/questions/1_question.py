'''
Age group ko classify karte hain:

Child: Agar age 13 se chhoti hai
Teenager: Agar age 13-19 ke beech hai
Adult: Agar age 20-59 ke beech hai
Senior: Agar age 60 ya usse zyada hai

'''

userInput = int(input("Kitne saal ka he be tu ? : "))

if(userInput < 13):
    print("Child")
elif(userInput < 20):
    print("Teenager")
elif(userInput < 60): 
    print("Adult")
else:
    print("Senior")

