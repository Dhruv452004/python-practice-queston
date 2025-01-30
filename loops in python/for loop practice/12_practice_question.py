'''
Question:

Ek list hai: numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]. 
Tumhe list ke saare prime numbers print karne hain.

'''

numbers = [2, 4, 5, 8, 11, 14, 17, 18, 23, 25]

for number in numbers:
    if(number > 1): #prime number 1 se bada hota h
        its_prime = True  # assume krte h ki prime true hai
        for i in range(2, number):
            if(number % i == 0):
               its_prime = False
               break  # Agar divisible mil gaya, to loop se bahar aa jao
        if(its_prime):
                print(f"Ye {number} prime number hai.")



# ise khete h nested loop yani loop ke andr loop
