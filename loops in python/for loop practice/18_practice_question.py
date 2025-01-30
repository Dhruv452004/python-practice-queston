'''
Prime Number Checker
Problem: Check if a number is prime.
'''

user_number = int(input("check kro number prime hai ya nahi: "))

is_prime = True

if(user_number >1):
    for num in range(2, user_number):
        if(user_number % num == 0 ):
            is_prime = False
            break
print(is_prime)

