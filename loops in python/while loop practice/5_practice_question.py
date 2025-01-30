'''
Question 5:
Tumhe 1 se lekar 100 tak ke numbers mein se sum of even 
numbers calculate karna hai using a while loop. Matlab, 2 + 4 + 6 + ... ka total 
calculate karna hai.

Hint:

Tum ek sum variable initialize kar sakte ho.
Tum start karoge 2 se (even number) aur har baar 2 se increment karte jaoge.
Jab tak number 100 se chhota ya barabar ho, loop chalega.
'''


# isko krne ke kafi trike h phele jo upr likha h vese krte h fir
# mein ek dusre trike se krke btaunga jisme if else ka use hoga

sum = 0
number = 2

while number <=100:
    sum += number
    number += 2


print(sum)