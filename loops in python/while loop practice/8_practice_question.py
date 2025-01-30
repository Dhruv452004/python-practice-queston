'''
Attempt problem 1 using while loop
'''


# isko thoda aur improve krte h jse ki agr isme koi 0 daal de ya koi string daal de
# tho use msg denge ki bhai ke kar rha h tu.

userInput = int(input("jis number ka table chaiye vo number daal: "))

number = 1
if userInput == 0:
    print("thara bhuut bna dunga saale 0 ka table nahi hota shi number daal")

else:
    while number <=10: 
        result = userInput * number
        print(f"{userInput} * {number} = {result}")
        number += 1