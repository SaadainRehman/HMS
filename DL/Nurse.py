from BL.Nurse import Nurse

class NurseDL:
    def __init__(self):
        self.nurses = []

    def add_nurse(self, name, shift, address, phone, salary, cnic, specialization, department):
        nurse = Nurse(name, shift, address, phone, salary, cnic, specialization, department)
        self.nurses.append(nurse)

    def get_nurses(self):
        return self.nurses
