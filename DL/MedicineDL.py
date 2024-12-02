from BL.Medicine import Medicine
class MedicineDL:
    def __init__(self):
        self.medicines = [
            Medicine("Aspirin", 5.0, "Pain reliever and anti-inflammatory"),
            Medicine("Paracetamol", 3.0, "Pain reliever and fever reducer"),
            Medicine("Amoxicillin", 10.0, "Antibiotic for bacterial infections"),
            Medicine("Ibuprofen", 7.0, "Anti-inflammatory and pain relief")
        ]

    def get_all_medicines(self):
        return self.medicines
