'''

Question 11: "Args_Kwargs_Summary"
Tumhe ek function banani hai jo multiple arguments (both normal arguments and keyword arguments) ko accept kare aur unka sum return kare. *args aur **kwargs ka use karna hoga. ek bar *args se solve kro and usi ke niche **kargs se bhi solve kro

'''

def multiple_arg(*args):
    return sum(args)
print(multiple_arg(2,2,2))


def multiple_kwarg(**kwargs):
    return sum(kwargs.values())
print(multiple_kwarg(num1 = 2, num2 = 2, num3 = 2, num4 = 2))