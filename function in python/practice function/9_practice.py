'''
Default Parameter Value
Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
'''

def greet(name = "loha"):
    return "Hello," + name
a = greet() # mene isme name nahi dia tho ye defult name se greet krega
b = greet("alice") # ab mene isme name dia tho ye is name ko print krega greet ke sath

print(f"{a}\n{b}")