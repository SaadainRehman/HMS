from BL.Staff import Staff

class Nurse(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, rank, ward_no, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._rank = rank  # Protected
        self._ward_no = ward_no  # Protected
        self._department = department  # Protected

    def check_patients(self):
        return f"Nurse {self._name} is checking patients in ward {self._ward_no}."
    
    def see_patients(self):
        return f"Nurse {self._name} is look aftering patients in ward {self._ward_no}."


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Rank: {self._rank}, Ward No: {self._ward_no}, Department: {self._department}"
