'''
Question 2: "Sum_Upto_N"
Tumhe ek loop ke through 1 se lekar N tak ke numbers ka sum calculate karna hai. Isme tum for loop use kar sakte ho.
'''

n = 10
for number in range(1, n + 1):
    number += n
print(number)


# dekho n ki value mene 10 di h yani loop tb 10 tk chlega tho number ki value bhi 10 ho jaygi 
# fir ye hoga number + n 10 + 10 = 20