'''

Simple Interest:
Ek program likho jo principal, rate of interest aur time input le aur simple interest calculate kare.

Principal (P) = 1000
Rate of Interest (R) = 5%
Time (T) = 2 years

Formula: Simple Interest = (P * R * T) / 100

'''

# User input
P = float(input("Enter Principal Amount: "))  # Principal
R = float(input("Enter Rate of Interest (%): "))  # Rate of Interest
T = float(input("Enter Time (years): "))  # Time

# Simple Interest formula
SI = (P * R * T) / 100

# Output
print("Simple Interest:", SI)
