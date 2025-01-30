'''
Question 4:"Factorial_Calculator"
Tumhe ek number ka factorial calculate karna hai. Tum for loop ka use karke factorial ka calculation kar sakte ho.
'''

number = int(input("enter number: "))
factorial = 1

for num in range(1, number +1):
    factorial *= num
print(f"factorial {number} iska hai = {factorial} ")