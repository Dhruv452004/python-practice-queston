'''

Age Calculator:
User ka birth year input le aur uska current age calculate karo.

'''
birth_year = int(input("enter your date of birth: "))
current_year = int(input("enter current year: "))

def age_calculator(birth_y, current_y):
    age =  current_y - birth_y 
    return age

calculate_age = age_calculator(birth_year, current_year)
print(f"aap  {calculate_age} saal ke hai")