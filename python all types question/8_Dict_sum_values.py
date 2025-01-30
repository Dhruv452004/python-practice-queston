'''
Question 8: "Dict_Sum_Values"
Tumhe ek dictionary diya gaya hai jisme numbers hain. Tumhe function banani hai jo dictionary ke saare values ka sum return kare.

num_dict = {'a': 10, 'b': 20, 'c': 30}
'''


def sum_func(n):
    return sum(n.values())
num_dict = {'a': 10, 'b': 20, 'c': 30}
print(sum_func(num_dict))