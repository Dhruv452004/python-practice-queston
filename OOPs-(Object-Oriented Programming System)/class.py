class Employee:  
    language = "Python"  # Yeh ek class attribute hai, jo har instance ke liye same rahega
    salary = 150  # Yeh bhi ek class attribute hai

# Ek naya Employee object banaya jiska naam 'loha' rakha
loha = Employee()  
loha.name = "Loha Jain"  # Yeh ek instance attribute hai, jo sirf 'loha' ke liye hoga

# 'loha' ke attributes ko print kiya
print(loha.name, loha.language, loha.salary)  
# Output: Loha Jain Python 150

# Ek aur Employee object banaya jiska naam 'laptop' rakha
laptop = Employee()  
laptop.name = "Laptop Kumar"  # Yeh bhi ek instance attribute hai, jo sirf 'laptop' ke liye hoga

# 'laptop' ke attributes ko print kiya
print(laptop.name, laptop.salary, laptop.language)  
# Output: Laptop Kumar 150 Python

# Note: 'name' har object ke liye alag ho raha hai kyunki yeh instance attribute hai,
# lekin 'language' aur 'salary' same hain kyunki yeh class attributes hain.
