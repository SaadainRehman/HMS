from BL.Staff import Staff

class Pharmacist(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._department = department

    def view_medicine_stock(self):
        return f"Pharmacist {self._name} is viewing the medicine stock."

    def dispense_medicine(self):
        return f"Pharmacist {self._name} is dispensing medicine."

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Department: {self._department}"
