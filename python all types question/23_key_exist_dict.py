'''

Question 23: "Key_Exist_Dict"
Tumhe ek dictionary aur ek key diya gaya hai. Tumhe ek function banani hai jo check kare ki diya gaya key dictionary mein exist karti hai ya nahi.

my_dict = {'a': 10, 'b': 20, 'c': 30}
key = 'b' # ye key check krni h

'''
def key_exist(dict, key):
    if(key in dict):
        return True
    else:
        return False

my_dict = {'a': 10, 'b': 20, 'c': 30}
key = 'b' # dekh ye key dict k andr h tho true return hoga
key2 = "sdfjkdsl" # dekh ab ye dekh ye dict ke andr nahi h tho ye false return krega
print(key_exist(my_dict, key))
print(key_exist(my_dict, key2))