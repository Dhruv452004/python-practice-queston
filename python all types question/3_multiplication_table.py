'''
Question 3: "Multiplication_Table"
Tumhe ek number ke multiplication table print karne hai. Tum for loop ka use karke 1 se 10 tak multiply karke print kar sakte ho.
'''

number = int(input("enter number: "))
for table in range(1, 11):
    result = number * table
    print(f"{number} x {table} = {result}")