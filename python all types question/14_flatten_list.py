'''

Question 14: "Flatten_List"
Tumhe ek nested list diya gaya hai, jaise [[1, 2], [3, 4], [5]]. Tumhe ek function banani hai jo is nested list ko flatten kare aur ek simple list return kare, jaise [1, 2, 3, 4, 5].

'''

nested_list = [[1, 2], [3, 4], [5]]
simple_list = []

def flatten_list():
    for i in nested_list:
        for list in i:
            simple_list.append(list)
    return simple_list

print(f"is nested list {nested_list} ko simple list mein bna dia dekho\n {flatten_list()}")