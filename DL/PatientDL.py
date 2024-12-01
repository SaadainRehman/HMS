class PatientDL:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patient_by_name(self, name):
        for patient in self.patients:
            if patient.get_name() == name:
                return patient
        return None

    def get_all_patients(self):
        return self.patients

    def update_patient(self, name, updated_patient):
        patient = self.get_patient_by_name(name)
        if patient:
            patient.set_name(updated_patient.get_name())
            patient.set_age(updated_patient.get_age())
            patient.set_phone(updated_patient.get_phone())
            patient.set_cnic(updated_patient.get_cnic())
            patient.set_address(updated_patient.get_address())
            patient.set_department(updated_patient.get_department())
            return True
        return False

    def delete_patient(self, name):
        patient = self.get_patient_by_name(name)
        if patient:
            self.patients.remove(patient)
            return True
        return False
