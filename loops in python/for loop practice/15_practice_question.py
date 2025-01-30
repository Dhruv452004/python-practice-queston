'''
 Multiplication Table Printer
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
'''

userNumber = int(input("enter number: "))
number = 0

for num in range(1, 11):
    result = userNumber * num
    number += result
    if(num == 5 ):
        continue
    print(f"5 x {num} = {result}")
