'''
Question 5: "Prime_Check"
Tumhe ek number check karna hai ki woh prime hai ya nahi. Tum for loop ka use karke divisors check kar sakte ho.
'''


number = int(input("enter number: "))
is_prime = True
for n in range(2, number):
    if(number % n == 0):
        is_prime = False
        break

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
