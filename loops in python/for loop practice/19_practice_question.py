'''
. List Uniqueness Checker
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]
'''

items = ["apple", "banana", "orange", "apple", "mango"]
duplicate_item = set()

for item in items:
    if(item in duplicate_item):
        print(f"duplicate {item}")
        break
    duplicate_item.add(item)