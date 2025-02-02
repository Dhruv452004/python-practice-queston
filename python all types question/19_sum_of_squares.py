'''

Question 19: "Sum_of_Squares"
Tumhe ek list of numbers diya gaya hai, jaise [1, 2, 3, 4]. Tumhe ek function banani hai jo list ke har number ka square le aur in sabka sum return kare.

'''
def sum_of_Squares():
    for i in range(1, len(num) +1):
       squares_value = (num[i - 1] ** 2)
       squares.append(squares_value)
       print(f"square of {num[i -1]} x {num[i -1]} = {squares_value}")
    return sum(squares)


num = [1, 2, 3, 4]
squares = []

sum_squares = sum_of_Squares()
# print(f"sum of squares {squares} = {sum_of_Squares()}") 
print(f"sum of squares {squares} = {sum_squares}")

