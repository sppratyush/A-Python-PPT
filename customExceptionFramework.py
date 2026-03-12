"""5.Custom Exception Framework 
Create your own custom exceptions for a specific application (like an Inventory 
Management System). 
For example: OutOfStockError, InvalidProductIDError, etc."""
class OutOfStockError(Exception):
    """Exception raised when a product is out of stock."""
    pass

class InvalidProductIDError(Exception):
    """Exception raised when a product ID is invalid."""
    pass
class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {"P001": 10, "P002": 5}

    def check_stock(self, product_id, quantity):
        if product_id not in self.inventory:
            raise InvalidProductIDError(f"Product ID {product_id} is invalid.")
        if self.inventory[product_id] < quantity:
            raise OutOfStockError(f"Product ID {product_id} is out of stock.")
        return True
# Example usage
if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()
    try:
        inventory_system.check_stock("P001", 5)  # This will pass
        inventory_system.check_stock("P002", 10)  # This will raise OutOfStockError
    except (OutOfStockError, InvalidProductIDError) as e:
        print("Error:", e)
    try:
        inventory_system.check_stock("P003", 1)  # This will raise InvalidProductIDError
    except (OutOfStockError, InvalidProductIDError) as e:
        print("Error:", e)
        