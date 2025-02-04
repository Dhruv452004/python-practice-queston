'''

Question 24: "Kwargs_Merge_Dicts"
Tumhe ek function banani hai jo multiple dictionaries ko **kwargs ka use karke merge kare aur ek final dictionary return kare.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

'''
def kwarg_function(**kwargs):
    result = {}
    for i in kwargs.values():
        result.update(i)

    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(kwarg_function(dict1 = dict1, dict2 = dict2))