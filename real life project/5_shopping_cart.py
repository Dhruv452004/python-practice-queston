'''

 Shopping Cart:
Ek shopping cart banao jisme different items aur unke prices ho, aur ek function banao jo total amount calculate kare.
Item 1: "Shirt" - 300 rs
Item 2: "Pants" - 500 rs
Item 3: "Shoes" - 200rs
'''
items = {
"Shirt": 300,
"Pants": 500,
"Shoes": 200
}


def shoping():
    total_amount = 0
    cart = []

    print("Ye items hamare paas available hain:")
    for key, value in items.items():
        print(f"{key}: {value}")
    
    print("\nEnter the items you want to buy (type 'done' to finish):")

    while True:
        key = input("Enter item name: ").title()
        if(key == "Done"):
            print("thank you")
            break
        elif(key in items):
            total_amount += items[key]
            cart.append((key, items[key]))
            print(f"{key} added to your cart.")
        else:
            print("Item not available. Please choose from the list.")  
    
    if cart:
        print("\nAapne ye saman liya hai:")
        for key, value in cart:
            print(f"{key}: {value}")  #

    print(f"\nYour total price is: ₹{total_amount}")  

shoping()