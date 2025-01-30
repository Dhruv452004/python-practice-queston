'''
Question:
Tumhe 7 ka table print karna hai, lekin iss baar jo result mile usko ek
 list mein store karna hai, aur phir us list ko print karna hai.

 ese [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
'''


seven_ki_list = list()

for seven in range(1, 11):
    result = 7 * seven
    seven_ki_list.append(result)
    # print(f"7 x {seven} = {result}")
    # check krte h ye 7 ka table list mein gya ya nahi

print(seven_ki_list)