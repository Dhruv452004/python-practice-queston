'''
Question:

Tumhare paas ek list hai: numbers = [5, 10, 15, 20, 25, 30]. 
Tumhe list ke saare even numbers print karne hain using a for loop.

'''

numbers = [5, 10, 15, 20, 25, 30]

for number in numbers:
    if(number % 2 == 0):
        print(f"ye {number} even number hai")