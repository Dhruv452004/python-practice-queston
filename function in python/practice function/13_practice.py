'''
Generator Function with yield
Problem: Write a generator function that yields even numbers up to a specified limit.
'''
def generator(limit):
    for i in range(2, limit+1, 2): 
        yield i
even_number = generator(10)
for number in even_number:
    print(number)



''' 
2 se shuru hoga aur limit mein jo number hoga tab tk chlega and uske baad usme 2 pluhota jayga jese muje 10 number kitne number even h vo print krna h 
tho ese uska process hoga
2
2+2 = 2
4+2 = 6
6+2 = 8
8+2 = 10
'''