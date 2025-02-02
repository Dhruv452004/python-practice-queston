'''

Question 18: "Dictionary_Keys_Values"
Tumhe ek dictionary diya gaya hai, my_dict = {'a': 1, 'b': 2, 'c': 3} Tumhe ek function banani hai jo dictionary ki keys aur values ko separately lists mein return kare.

'''

my_dict = {'a': 1, 'b': 2, 'c': 3}

def seperate_key_value():
    keys = (my_dict.keys())
    values = (my_dict.values())
    return keys, values

my_keys, my_values = seperate_key_value()
print(f"{my_dict} ko seperate krke keys aur values ayi h \n {my_keys}\n aur {my_values}")
