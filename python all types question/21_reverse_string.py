'''

Question 20: "Reverse_String"
Tumhe ek string diya gaya hai, jaise "loha". Tumhe ek function banani hai jo is string ko reverse kare aur result return kare, bina built-in reverse functions ka use kiye.

'''



def reverse_string(a):
    reverse_str = a[::-1]
    return reverse_str

str = "loha"
print(reverse_string(str))