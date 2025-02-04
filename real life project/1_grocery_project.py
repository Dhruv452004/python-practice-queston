'''
Grocery List: 
Ek grocery list banao jisme items aur unki prices ho. Phir total price calculate karo.

'''

# Grocery list jisme items aur unke prices hain
grocery_list = {
    'Rice': 50,
    'Wheat Flour': 40,
    'Sugar': 30,
    'Salt': 10,
    'Oil': 120,
    'Milk': 40,
    'Eggs': 60
}

# Ye main function hai jo total price calculate karega
def calculate_total():
    total_price = 0
    item_selected = []  # Jo items select kiye jaenge, unka list
    print("Ye items hamare paas available hain:")
    print("\n" + "*" * 50)  # Yeh line sirf design ke liye hai
    for item, price in grocery_list.items():
        print(f"{item}: ₹{price}")  # Yeh print karega ki kaunse item available hain aur unka price kitna hai

    print("\n" + "*" * 50)  # Yeh line design ke liye hai
    print("\nEnter the items you want to buy (type 'done' to finish):")  # Yeh message user ko batata hai ki woh kis item ko select kar sakte hain

    while True:
        item = input("Enter item name: ").title()  # User input lega aur item ko title case mein convert karega
        if(item == "Done"):  # Agar user 'done' type kare, toh loop break ho jayega
            break
        elif(item in grocery_list):  # Agar user ne available item select kiya hai
            total_price += grocery_list[item]  # Jo item select hoga, uska price total mein add hoga
            item_selected.append((item, grocery_list[item]))  # Selected item ko item_selected list mein add karega

            print(f"{item} added to your cart.")  # Item cart mein add hone par confirmation print hoga
        else:
            print("Item not available. Please choose from the list.")  # Agar item grocery list mein nahi hai, toh ye message dikhayega

    if item_selected:  # Agar koi item select kiya gaya ho
        print("\n" + "*" * 80)  # Yeh line design ke liye hai
        print("\nAapne ye saman liya hai:")  # Yeh message show karega ki user ne kaunse items select kiye hain
        for item, price in item_selected:
            print(f"{item}: {price}")  # Selected items ka naam aur price display karega
        print("\n" + "*" * 80)  # Yeh line design ke liye hai

    print("\n" + "--" * 20)  # Yeh line design ke liye hai
    print(f"\nYour total price is: ₹{total_price}")  # Total price return karega

# Function call karein
calculate_total()
print("\n" + "--" * 20)  # Yeh line design ke liye hai




