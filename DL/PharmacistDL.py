from BL.Pharmacist import Pharmacist

class PharmacistDL:
    def __init__(self):
        self.pharmacists = []

    def add_pharmacist(self, name, shift, address, phone, salary, cnic, department):
        pharmacist = Pharmacist(name, shift, address, phone, salary, cnic, department)
        self.pharmacists.append(pharmacist)

    def get_pharmacists(self):
        return self.pharmacists
