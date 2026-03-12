"""4.E-Commerce Order Management 
Manage orders, returns, and refunds. 
Handle cases like invalid coupon code, out-of-stock errors, invalid payment 
methods."""
class ECommerceOrderManagement:
    def __init__(self):
        self.orders = {}
        self.stock = {"item1": 10, "item2": 5}
        self.coupons = {"DISCOUNT10": 0.1}

    def place_order(self, order_id, item, quantity, coupon_code=None):
        if item not in self.stock:
            raise KeyError("Item does not exist.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self.stock[item] < quantity:
            raise ValueError("Out of stock.")
        discount = self.coupons.get(coupon_code, 0)
        total_price = quantity * 100 * (1 - discount)  # Assuming each item costs 100
        self.orders[order_id] = {"item": item, "quantity": quantity, "total_price": total_price}
        self.stock[item] -= quantity

    def return_order(self, order_id):
        if order_id not in self.orders:
            raise KeyError("Order ID does not exist.")
        order = self.orders.pop(order_id)
        self.stock[order["item"]] += order["quantity"]

    def refund_order(self, order_id):
        if order_id not in self.orders:
            raise KeyError("Order ID does not exist.")
        order = self.orders[order_id]
        return order["total_price"]
# Example usage
if __name__ == "__main__":
    order_manager = ECommerceOrderManagement()
    try:
        order_manager.place_order("O001", "item1", 2, "DISCOUNT10")
        print(order_manager.orders)  # Output: {'O001': {'item': 'item1', 'quantity': 2, 'total_price': 180.0}}
        order_manager.return_order("O001")
        print(order_manager.orders)  # Output: {}
        order_manager.refund_order("O001")  # This will raise an exception
    except (ValueError, KeyError) as e:
        print("Error:", e)
        