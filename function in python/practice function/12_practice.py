'''
 Function with **kwargs
Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
'''


def student_detail(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f"{key}: {value}")
    return result
result = student_detail(name = "rahu", age = 20, grade = "A")
print(result)
