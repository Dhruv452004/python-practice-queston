'''

Question 16: "Common_Elements"
Tumhe do lists diya gaya hain. list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6] Tumhe ek function banani hai jo in dono lists ke common elements ko find kare aur return kare

'''


def common_elements():
    for element in list1:
          if(element in list2):
            common.append(element)
    return common

common = []
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(common_elements())




# set ki madad se

# def common_ele(set1, set2):
#     common = set1.intersection(set2)
#     common = list(common)
#     return common

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]


# # list ko set mein convert kra


# list1 = set(list1)
# list2 = set(list2)

print(common_ele(list1, list2))

