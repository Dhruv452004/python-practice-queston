'''

Question 12: "List_Reverse"
Tumhe ek list diya gaya hai, jaise [1, 2, 3, 4, 5]. Tumhe ek function banani hai jo is list ko reverse kare aur result ko return kare bina built-in reverse functions ka use kiye.

'''


num = [1, 2, 3, 4, 5]
reverse_num = []

def reverse_list():
    for i in range(len(num)-1, -1, -1):
        reverse_num.append(num[i])
    return reverse_num

print(f"{num} iska reverse hai {reverse_list()}")





