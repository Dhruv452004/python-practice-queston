'''
 Password Strength Checker
Problem: Check if a password is "Weak", "Medium", or "Strong". 
Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

chars mtlb charactor jese => (loha danger)

'''


password = (input("check kr ki tera password weak, medium, strong mein se kesa h: "))

if(len(password) < 6):
    print(f"bade bhai apka password {password} weak hai")
elif(len(password) <= 10):
    print(f"bade bhai apka password {password} medium hai")
else:
    print(f"bade bhai apka password {password} strong")
