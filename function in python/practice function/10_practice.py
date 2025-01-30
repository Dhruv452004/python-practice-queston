'''
Lambda Function
Problem: Create a lambda function to compute the cube of a number.

Lambda function ek short function hota hai jo ek line mein likha jata hai. Is case mein, tumhe ek aise function ki zarurat hai jo kisi number ko cube (matlab us number ko 3 times multiply) kare.

Ek hint: Tum lambda function mein ek input parameter loge (jaise x), aur fir uska cube return karoge, jo ki x**3 ho sakta hai.


Lambda function ka syntax kuch is tarah hota hai:
lambda arguments: expression


'''


x = int(input("enter number: "))

cube = lambda x: x**3

a = cube(x)
print(a)
