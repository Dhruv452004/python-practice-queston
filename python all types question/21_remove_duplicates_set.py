'''

Question 21: "Remove_Duplicates_Set"
Tumhe ek list diya gaya hai, jaise:
numbers = [1, 2, 2, 3, 4, 4, 5]
Tumhe ek function banani hai jo list se duplicates hata kar ek unique elements ki sorted list return kare.

'''


def duplicate():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_element = sorted(set(numbers))
    return unique_element
print(duplicate())
