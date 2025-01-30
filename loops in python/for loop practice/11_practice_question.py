'''
Question:

Ek list hai: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Tumhe list ke elements ko check karna hai aur agar
number 4 se zyada ho toh unko "Greater than 4" print karna hai. 
Baaki elements ko "Less than or equal to 4" print karna hai.

'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if(number > 4):
        print(f"Greater than 4 numbers hai {number}")

    elif(number < 4 or number == 4):
        print(f"Less than or equal to 4 numbers hai {number}")
