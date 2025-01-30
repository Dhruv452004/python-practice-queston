'''
write a python program using function to convert celsius to fahrenheit
'''


def celsius_to_fahrenheit(celsius):
    Fahrenheit = (celsius * 9/5) + 32 # ye formual h ye google pr mil jayga
    return Fahrenheit

userInput = float(input("Convert celcius to fahrenheit: "))

result = celsius_to_fahrenheit(userInput)
print(result)
