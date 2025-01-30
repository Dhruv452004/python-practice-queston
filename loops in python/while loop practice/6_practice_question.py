'''
 Factorial Calculator
Problem: Compute the factorial of a number using a while loop.

factorial kese niklta h dekho jese 5 ka factorial kya hoga

5*4*3*2*1

5*4 = 20
5*4*3 = 60
5*4*3*2 = 120
5*4*3*2*1 = 120

'''
# while loop
userInput = int(input("enter number: "))
factorial = 1 
youChoose = userInput
# jb userinput 0 ho jayga loop exit ho jayga jis karan print krate samay userinput 0 show hoga islye mein ise ek variable mai store kra rha hu taki ye vo value print kre jo user ne choose kri h

while(userInput > 0):
    factorial *= userInput
    userInput -= 1
print(f"Factorial of {youChoose} is {factorial}")


# ye for loop mein ese hoga

# userInput = int(input("enter number: "))
# factorial = 1

# for number in range(1, userInput+1):
#     factorial *= number
# print(f"Factorial of {userInput} is {factorial}")