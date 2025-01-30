'''
How do you prevent a python print() function to print a new line at the end
'''

print("Hello")
print("World!")


print("Hello", end="")
print("World!")



print('hello\nworld')



'''
Agar tum print() function use karte ho Python mein aur 
chahte ho ki wo new line na print kare, toh tum end parameter 
ka use kar sakte ho. By default, print() function ke baad ek 
newline character \n hota hai. Agar tumhe isko avoid karna hai, 
toh end="" ya kisi aur string value ke saath specify kar do.
'''