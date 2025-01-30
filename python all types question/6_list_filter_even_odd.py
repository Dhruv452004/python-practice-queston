'''
Question 6: "List_Filter_Even_Odd"
Tumhe ek list diya gaya hai jisme numbers hain. Tumhe ek function banana hai jo list ko filter kare aur even numbers ko ek list mein aur odd numbers ko doosre list mein daale.
'''

numbers = [13, 6, 9, 4, 15, 8, 3, 12, 7, 10]

def is_even_or_odd(numbers):
        even_list = list(filter(lambda x: x % 2 == 0, numbers))
        odd_list = list(filter(lambda x: x % 2 != 0, numbers))
        return even_list, odd_list
result = is_even_or_odd(numbers)
print(result)