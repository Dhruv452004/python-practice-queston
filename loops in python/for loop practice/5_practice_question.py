'''
Question:
Tumhe 3 ka table print karna hai lekin har number ke baad 
uska square bhi print karna hai. Jaise:

mathematica
Copy
Edit
3 x 1 = 3, Square = 9
3 x 2 = 6, Square = 36
...
Hint:

Tum multiplication karne ke baad uska square bhi calculate karna hoga using ** operator.
'''


for three_table in range(1, 11):
    result = 3 * three_table
    square = result ** 2
    print(f"3 x {three_table} = {result}, Square = {square}")

