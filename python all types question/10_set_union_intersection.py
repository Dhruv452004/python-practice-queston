'''
Question 10: "Set_Union_Intersection"
Tumhe do sets diye gaye hain. Tumhe ek function banani hai jo un dono sets ka union aur intersection return kare.

num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7, 8}

'''



num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7, 8}
def set_union_intersection(set1, set2):
    result1 = set1.union(set2)
    result2 = set1.intersection(set2)
    return result1, result2


union, intersection  = set_union_intersection(num1, num2)

print(f"union = {union}")
print(f"intersection = {intersection}")