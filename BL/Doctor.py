from BL.Staff import Staff

class Doctor(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, specialization, experience, availability, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._specialization = specialization  # Protected
        self._experience = experience  # Protected
        self._availability = availability  # Protected
        self._department = department  

    def see_patients(self):
        return f"Dr. {self._name} is seeing patients."

    def charge_medicine(self):
        return f"Dr. {self._name} is charging for medicine."
    
    def check_patients(self):
        return f"Dr. {self._name} is checking patients."
    

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Specialization: {self._specialization}, Experience: {self._experience}, Availability: {self._availability}, Department: {self._department}"
