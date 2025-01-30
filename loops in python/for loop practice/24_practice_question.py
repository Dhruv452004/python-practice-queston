'''
Write a program to print the following star pattern

         *
        ***
       *****
'''






row = 3

for number in range(1, row + 1):
    print(" " * (row - number), end = "")
    print("*" * (2* number - 1))
