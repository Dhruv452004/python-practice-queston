'''
Question 2:
Tumhe 2 ka table print karna hai using a while loop. Jaise:

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
2 x 10 = 20
Hint:
Ek counter variable initialize karo (e.g., i = 1).
Jab tak counter 10 se chhota ya barabar ho, tab tak loop chalana hai.
Har iteration mein counter ko increment karte jaana.
'''

number = 1

while number <=10:
    result = number * 2
    print(f"2 x {number} = {result}")
    number +=1


