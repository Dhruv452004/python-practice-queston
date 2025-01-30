'''
Write a recursive function to calculate the sum of first n natural number

recursive ke liye ye formual h

n(n-1) + n
'''

def sum_of_natural(n):
    if(n == 1): #base 1
        return 1
    else:
        return sum_of_natural(n-1) + 2 # Recursive call
    
n = int(input("enter number: "))

sum = sum_of_natural(n)
print(sum)

