#Track goods movement, generate inventory reports, and forecast demand.
class Warehouse:
    def __init__(self):
        self.inventory = {}
    
    def add_goods(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    
    def remove_goods(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            return True
        return False
    
    def generate_report(self):
        report = "Inventory Report:\n"
        for item, quantity in self.inventory.items():
            report += f"{item}: {quantity}\n"
        return report
    
    def forecast_demand(self, item, historical_data):
        # Simple forecasting based on average demand
        if item in historical_data:
            average_demand = sum(historical_data[item]) / len(historical_data[item])
            return average_demand
        return 0
if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.add_goods("Item A", 100)
    warehouse.add_goods("Item B", 50)
    warehouse.remove_goods("Item A", 20)
    print(warehouse.generate_report())
    historical_data = {
        "Item A": [20, 30, 25, 35],
        "Item B": [10, 15, 12, 18]
    }
    print(f"Forecasted demand for Item A: {warehouse.forecast_demand('Item A', historical_data)}")
    print(f"Forecasted demand for Item B: {warehouse.forecast_demand('Item B', historical_data)}")
    