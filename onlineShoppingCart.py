
products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Smartphone", "price": 20000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1500},
    5: {"name": "Mouse", "price": 800},
    6: {"name": "Cooler", "price": 1200},
    7: {"name": "Monitor", "price": 15000},
    8: {"name": "Tablet", "price": 10000},
    9: {"name": "Smartwatch", "price": 5000},
    10: {"name": "Hard Drive", "price": 4000},
    11: {"name": "USB", "price": 500},
    12: {"name": "Webcam", "price": 2500},
    13: {"name": "Microphone", "price": 3000},
    14: {"name": "Speakers", "price": 3500},
    15: {"name": "Router", "price": 4500}
}

cart = {}

def show_products():
    print("\nAvailable Products:")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - ₹{details['price']}")

def add_to_cart():
    pid = int(input("Enter product ID to add: "))
    if pid in products:
        qty = int(input("Enter quantity: "))
        if pid in cart:
            cart[pid] += qty
        else:
            cart[pid] = qty
        print("Item added to cart!")
    else:
        print("Invalid Product ID!")

def remove_from_cart():
    pid = int(input("Enter product ID to remove: "))
    if pid in cart:
        del cart[pid]
        print("Item removed from cart!")
    else:
        print("Item not in cart!")

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return
    
    print("\nYour Cart:")
    total = 0
    for pid, qty in cart.items():
        name = products[pid]["name"]
        price = products[pid]["price"]
        subtotal = price * qty
        total += subtotal
        print(f"{name} | ₹{price} x {qty} = ₹{subtotal}")
    
    print(f"\nTotal Amount: ₹{total}")

def checkout():
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return
    view_cart()
    print("\nOrder placed successfully!")
    cart.clear()

while True:
    print("\n===== Online Shopping Cart =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice! Try again.")