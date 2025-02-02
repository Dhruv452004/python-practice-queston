'''

Question 15: "Max_Min_Tuple"
Tumhe ek tuple diya gaya hai, jaise (3, 7, 2, 8, 1). Tumhe ek function banani hai jo is tuple se maximum aur minimum values ko return kare.

'''
num = (3, 7, 2, 8, 1)

def max_min_tuple():
    sorted_num = sorted(num)
    min_num = sorted_num[0]
    max_num = sorted_num[-1]
    return max_num, min_num

max_number, min_number = max_min_tuple()
print(f"is {num} mein se max number hai {max_number} aur min number hai {min_number}")

