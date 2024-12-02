from BL.Staff import Staff

class Pharmacist(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic):
        super().__init__(name, shift, address, phone, salary, cnic)

    def view_medicine(self):
        return f"Pharmacist {self.name} is viewing the medicine stock."

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Role: Pharmacist"
