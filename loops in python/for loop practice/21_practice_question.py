'''
Write a program to greet all the person names stored
in a list l1 and which start with 5
 '''

l1 = ["5John", "Alice", "5Mark", "Bob", "5Alex"]
for naam in l1:
    if naam.startswith("5"):
        print(f"ram ram {naam} bhai")