from BL.Staff import Staff

class Pharmacist(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._department = department
        self._medicine_stock = [
            {"name": "Paracetamol", "quantity": 100},
            {"name": "Ibuprofen", "quantity": 80},
            {"name": "Ciprofloxacin", "quantity": 60},
            {"name": "Amoxicillin", "quantity": 50},
            {"name": "Metformin", "quantity": 70},
        ]

    def view_medicine_stock(self):
        if not self._medicine_stock:
            return "Medicine stock is empty."
        result = "\n--- Medicine Stock ---\n"
        for idx, medicine in enumerate(self._medicine_stock, start=1):
            result += f"{idx}. Medicine: {medicine['name']}, Quantity: {medicine['quantity']}\n"
        return result

    def dispense_medicine(self, medicine_name, quantity):
        for medicine in self._medicine_stock:
            if medicine["name"].lower() == medicine_name.lower():
                if medicine["quantity"] >= quantity:
                    medicine["quantity"] -= quantity
                    return f"Dispensed {quantity} units of {medicine_name}."
                else:
                    return f"Insufficient stock for {medicine_name}."
        return f"Medicine {medicine_name} not found in stock."

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Department: {self._department}"
