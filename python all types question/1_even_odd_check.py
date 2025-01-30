'''
Question 1: "Even_Odd_Check"
Tumhe ek loop use karna hai jo list ke har element ko check kare aur print kare ki woh even hai ya odd.
'''


numbers = int(input("enter number: "))
for number in range(1, numbers + 1):
    if(number % 2 == 0):
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")