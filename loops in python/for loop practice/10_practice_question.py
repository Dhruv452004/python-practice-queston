'''
Question:

Ek list hai: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
Tumhe list ke elements ko 3 se divide karke jo result mile usko print karna hai, 
bas unhi elements ko jinmein remainder 0 ho.

'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if(number % 3 == 0):
        print(number)
        
        
