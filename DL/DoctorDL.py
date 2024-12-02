from BL.Doctor import Doctor
class DoctorDL:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, name, shift, address, phone, salary, cnic, specialization, experience, availability, department):
        doctor = Doctor(name, shift, address, phone, salary, cnic, specialization, experience, availability, department)
        self.doctors.append(doctor)

    def get_doctors(self):
        return self.doctors

