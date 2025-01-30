'''
Counting Positive Numbers
Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

yani ye numbers list mein jitne positive numbers h vo total kitne h unka count dena h

'''

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0 # isme vo number count honge jo positive honge shuru mein ise 0 kra h mene

for number in numbers:
    if(number > 0):
        positive_number_count += 1
        print(f"ye rhe positive numbers = {number} ") # isme vo numbers print hoge jo positive h question mein bola nahi h lekin mein tb bhi print kra rha hu

print(f"\ntotal count of positive numbers is = {positive_number_count}")

