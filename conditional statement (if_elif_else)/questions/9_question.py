'''
 Leap Year Checker
Problem: Determine if a year is a leap year. (Leap years are divisible by 4, 
but not by 100 unless also divisible by 400).

'''

print("check kr ki konse saal mein leap year h ya nahi")

year = int(input("\nenter year: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
