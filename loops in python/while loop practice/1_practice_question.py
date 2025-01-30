'''
Question 1:
Tumhe 10 tak ke numbers ka sum calculate karna hai 
using a while loop. Matlab, 1 + 2 + 3 + ... + 10 ka total calculate karna hai.

Hint:

Tum ek sum variable initialize kar sakte ho.
Har iteration mein sum ko update karna hoga aur counter ko increment karte jaana hoga.
'''

numbers = 1
total_sum = 0

while numbers <=10:
    total_sum += numbers
    numbers += 1
print(f"Sum of numbers from 1 to 10 = {total_sum}")


