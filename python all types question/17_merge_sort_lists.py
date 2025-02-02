'''

Question 17: "Merge_Sort_Lists"
Tumhe do sorted lists diya gaya hain. list1 = [1, 4, 6], list2 = [2, 3, 5] Tumhe ek function banani hai jo in dono lists ko merge kare aur ek sorted list return kare.

'''


list1 = [1, 4, 6]
list2 = [2, 3, 5]

def merge_sort(a, b):
    a.extend(b)
    a.sort()
    return a
print(merge_sort(list1, list2))    
