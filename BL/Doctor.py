from BL.Staff import Staff

class Doctor(Staff):
    def __init__(self, name, shift, address, phone, salary, cnic, specialization, experience, availability, department):
        super().__init__(name, shift, address, phone, salary, cnic)
        self._specialization = specialization
        self._experience = experience
        self._availability = availability
        self._department = department
        self._assigned_patients = [
            {"name": "Ali Khan", "age": 45, "condition": "Diabetes"},
            {"name": "Fatima Ahmed", "age": 28, "condition": "Flu"},
            {"name": "Hassan Raza", "age": 60, "condition": "Hypertension"},
            {"name": "Sara Malik", "age": 35, "condition": "Migraine"},
        ]
        self._schedule = [
            {"day": "Monday", "shift": "Outpatient Consultation"},
            {"day": "Tuesday", "shift": "Inpatient Rounds"},
            {"day": "Wednesday", "shift": "Surgery"},
            {"day": "Thursday", "shift": "Consultations"},
            {"day": "Friday", "shift": "Emergency Department"},
            {"day": "Saturday", "shift": "Special Clinic"},
        ]

    def see_patients(self):
        return f"Dr. {self._name} is seeing patients."

    def view_assigned_patients(self):
        if not self._assigned_patients:
            return "No patients assigned."
        result = "\n--- Assigned Patients ---\n"
        for idx, patient in enumerate(self._assigned_patients, start=1):
            result += f"{idx}. Name: {patient['name']}, Age: {patient['age']}, Condition: {patient['condition']}\n"
        return result

    def update_patient_records(self, patient_index, updated_condition):
        if 0 <= patient_index < len(self._assigned_patients):
            self._assigned_patients[patient_index]["condition"] = updated_condition
            return f"Patient record updated: {self._assigned_patients[patient_index]}"
        else:
            return "Invalid patient index."
        
    def view_schedule(self):
        if not self._schedule:
            return "No schedule available."
        
        result = "\n--- Weekly Schedule ---\n"
        for day in self._schedule:
            result += f"{day['day']}: {day['shift']}\n"
        
        return result


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Specialization: {self._specialization}, Experience: {self._experience}, Availability: {self._availability}, Department: {self._department}"
