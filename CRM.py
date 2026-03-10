#Store customer info, manage communication logs, and track sales pipelines
class CRM:
    def __init__(self):
        self.customers = {}
        self.communication_logs = []
        self.sales_pipeline = []
    def add_customer(self, customer_id, customer_info):
        self.customers[customer_id] = customer_info
    def log_communication(self, customer_id, communication):
        self.communication_logs.append((customer_id, communication))
    def track_sales_pipeline(self, customer_id, stage):
        self.sales_pipeline.append((customer_id, stage))
if __name__ == "__main__":
    crm = CRM()
    crm.add_customer(1, {"name": "Pratyush", "email": "pratyush@egmail.com"})
    crm.log_communication(1, "Called customer to follow up on project.")
    crm.track_sales_pipeline(1, "Prospecting")
    print("Customers:", crm.customers)
    print("Communication Logs:", crm.communication_logs)
    print("Sales Pipeline:", crm.sales_pipeline)
