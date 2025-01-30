'''
Grade Calculator
Problem: Assign a letter grade based on a student's score: 
A grade (90-100), 
B grade (80-89), 
C grade (70-79), 
D grade (60-69), 
F grade (40-59).
fail (40 se kam vale)
'''


score = int(input("chl be apna score daal: "))

# dekho mene score mein set kra h ki agr 90 ya 90 se jada hoga score tho A grade print hoga ab agr koi 100 se bhi jada score dala dega jese (111,22233) tho bhi ye use A grade dega tho use theek krenge uske liye ek if conditon lga denge jisme use khedene ki bhai agr tune 100 se jada score dala tho tuje ek msg ayga.


if(score > 100):
    print("bete aukat mein score daal ke nahi tho kaan par rhepat bhaut tej pdega")
    exit() # exit() se niche vali condition nahi chlegi agr ye conditon true hoti h tho

if(score >= 90):
    print("A grade")
elif(score >= 80):
    print("B grade")
elif(score >= 70):
    print("C grade")
elif(score >= 60):
    print("D grade")
elif(score >= 40):
    print("F grade")
else:
    print("are bhai agle saal mehnat krio tu fail ho gya hai")

