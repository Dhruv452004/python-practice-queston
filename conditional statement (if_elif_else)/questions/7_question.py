'''
Coffee Customization
Problem: Customize a coffee order: "Small", "Medium", or "Large" 
with an option for "Extra shot" of espresso.

'''

size = input("Apne coffee size ko choose karo (Small, Medium, Large):").capitalize()

extra_shot = input("Kya aap extra shot of espresso chahte hain? (y/n):").lower()

coffee_order = ""

if(size == "Small"):
    coffee_order = "Small"
elif(size =="Medium"):
    coffee_order = "Medium"
elif(size =="Large"):
    coffee_order = "Large"
else:
    print("coffee ka size shi se daal nalle ")

# exra shot of espresso

if(extra_shot == "y"):
    coffee_order += " with extra_shot of espresso"
elif(extra_shot == "n"):
    coffee_order
else:
    print("abe y/n mein se koi ek daal nalle")


print(f"apka coffree order hai {coffee_order}")