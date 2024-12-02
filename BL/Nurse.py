from BL.Staff import Staff

class Nurse(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, specialization, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._specialization = specialization
        self._department = department

    def assist_doctor(self):
        return f"Nurse {self._name} is assisting in {self._department}."

    def check_vitals(self):
        return f"Nurse {self._name} is checking patients' vitals."

    def administer_medicine(self):
        return f"Nurse {self._name} is administering medicine."

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Specialization: {self._specialization}, Department: {self._department}"
