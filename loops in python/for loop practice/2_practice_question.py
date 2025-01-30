
'''
Question:
Tumhe 5 ka table print karna hai, lekin har result ko sum me add karte jaana hai. Matlab, jaise:

5 x 1 = 5
5 x 2 = 10
...
Sum of results = ...
Tum for loop ka use karo, aur sum variable ko update karte raho.

Hint:
Tumhe ek sum variable create karna hoga aur har iteration mein usko update karna hoga.
Final sum ko print karna na bhoolna!
'''

sum_of_result = 0

for table in range(1, 11):
    result = 5 * table
    sum_of_result += result
    print(f"5 x {table} = {result}")

