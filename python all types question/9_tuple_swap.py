'''
Question 9: "Tuple_Swap"
Tumhe ek tuple diya gaya hai. Tumhe ek function banani hai jo tuple ke pehle aur last elements ko swap kare.
'''

fruits = ("apple", "banana", "mango", "guava", "pineapple")
fruit_list = list(fruits)

def swap():
    fruit_list[0], fruit_list[4] = fruit_list[4], fruit_list[0]
swap()
fruit_list = tuple(fruit_list)
print(fruit_list)
