# ye mene ai se kraya ki ye gui mein show ho bs ese hi check krne k liye
'''
Python GUI Frameworks:
Aap Python ke GUI frameworks jaise Tkinter ya Kivy use kar sakte hain, jisse aap apna app bana sakte hain jo graphical interface ke saath chalega. Ye app aapke laptop pe normal app ki tarah chalega.

Tkinter Example: Tkinter ek simple aur lightweight GUI library hai, jo aapko window, buttons, text boxes aur labels create karne ki facility deta hai. Aapka program terminal ki jagah ek window mein run karega.
'''

import tkinter as tk
from tkinter import messagebox

# Grocery list dictionary
grocery_list = {
    'Rice': 50,
    'Wheat Flour': 40,
    'Sugar': 30,
    'Salt': 10,
    'Oil': 120,
    'Milk': 40,
    'Eggs': 60
}

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery List")
        self.total_price = 0
        self.items_selected = []

        self.label = tk.Label(root, text="Select items to buy:")
        self.label.pack()

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        for item in grocery_list:
            self.listbox.insert(tk.END, item)
        self.listbox.pack()

        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()

        self.total_label = tk.Label(root, text="Total Price: ₹0")
        self.total_label.pack()

        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)
        self.checkout_button.pack()

    def add_to_cart(self):
        selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
        for item in selected_items:
            self.items_selected.append(item)
            self.total_price += grocery_list[item]
        self.total_label.config(text=f"Total Price: ₹{self.total_price}")

    def checkout(self):
        if self.items_selected:
            items = "\n".join(self.items_selected)
            messagebox.showinfo("Checkout", f"You selected:\n{items}\nTotal Price: ₹{self.total_price}")
        else:
            messagebox.showwarning("No Items", "No items selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()
