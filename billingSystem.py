import datetime

class Product:
    """Represents a product available in the store."""
    def __init__(self, product_id, name, price):
        self.product_id = str(product_id)
        self.name = name
        self.price = float(price)

class Bill:
    """Represents a customer's shopping cart and final invoice."""
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = [] # List to hold cart items
        self.date_time = datetime.datetime.now()

    def add_item(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        self.items.append({'product': product, 'qty': quantity})
        print(f"Added {quantity}x {product.name} to {self.customer_name}'s bill.")

    def generate_receipt(self, tax_rate=0.05, discount_pct=0.0):
        if not self.items:
            print("The cart is empty. No receipt to generate.")
            return

        print("\n" + "="*50)
        print(f"{'SUPERMART RETAIL INVOICE':^50}")
        print("="*50)
        print(f"Date: {self.date_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Customer: {self.customer_name}")
        print("-" * 50)
        print(f"{'Item Name':<20} | {'Qty':<5} | {'Price':<8} | {'Total':<8}")
        print("-" * 50)
        
        subtotal = 0.0
        for item in self.items:
            prod = item['product']
            qty = item['qty']
            total_price = prod.price * qty
            subtotal += total_price
            print(f"{prod.name:<20} | {qty:<5} | ${prod.price:<7.2f} | ${total_price:<7.2f}")
        
        print("-" * 50)
        discount_amount = subtotal * discount_pct
        after_discount = subtotal - discount_amount
        tax_amount = after_discount * tax_rate
        grand_total = after_discount + tax_amount

        print(f"{'Subtotal:':<39} ${subtotal:>7.2f}")
        if discount_pct > 0:
            print(f"{f'Discount ({discount_pct*100}%):':<39} -${discount_amount:>7.2f}")
        print(f"{f'Tax ({tax_rate*100}%):':<39} ${tax_amount:>7.2f}")
        print("=" * 50)
        print(f"{'GRAND TOTAL:':<39} ${grand_total:>7.2f}")
        print("=" * 50)
        print(f"{'Thank you for shopping with us!':^50}\n")


class StoreSystem:
    """Manages the overall store inventory."""
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, name, price):
        self.inventory[str(product_id)] = Product(product_id, name, price)

    def get_product(self, product_id):
        return self.inventory.get(str(product_id))


# ==========================================
# Demonstration of the Billing System
# ==========================================
if __name__ == "__main__":
    # 1. Initialize the store and add inventory
    store = StoreSystem()
    store.add_product("101", "Whole Wheat Bread", 2.50)
    store.add_product("102", "Organic Milk (1L)", 1.80)
    store.add_product("103", "Free-Range Eggs", 3.20)
    store.add_product("104", "Arabica Coffee", 8.50)
    store.add_product("105", "Apples (1kg)", 4.00)

    print("Store inventory loaded successfully.\n")

    # 2. Create a new bill for a customer
    customer_bill = Bill("Alice Johnson")

    # 3. Simulate a checkout process by fetching items via Product ID
    cart_requests = [
        ("101", 2), # 2 loaves of bread
        ("104", 1), # 1 bag of coffee
        ("105", 3), # 3 kg of apples
        ("999", 1)  # Invalid product ID to test error handling
    ]

    for prod_id, qty in cart_requests:
        product = store.get_product(prod_id)
        if product:
            customer_bill.add_item(product, qty)
        else:
            print(f"Error: Product ID '{prod_id}' not found in inventory.")

    # 4. Generate the final receipt (with a 5% tax and 10% discount)
    customer_bill.generate_receipt(tax_rate=0.05, discount_pct=0.10)    