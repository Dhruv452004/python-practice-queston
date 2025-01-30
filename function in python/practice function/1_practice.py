'''
Write a program using function to find greatest of three numbers
'''

# max() ye method se hm kisi bhi list tuple etc mein se greatest number nikal skte h

def greatest_number():
    number = [1, 2, 30, 4, 99, 0, 200]
    return max(number)

print(greatest_number())