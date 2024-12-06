from BL.Medicine import Medicine

class MedicineDL:
    def __init__(self):
        self.medicines = [
            Medicine("Panadol", 3.0, "Pain reliever and fever reducer"),
            Medicine("Brufen", 5.0, "Anti-inflammatory and pain reliever"),
            Medicine("Caflam", 6.0, "Pain reliever and anti-inflammatory"),
            Medicine("Tonoflex", 8.0, "Relief for joint and muscular pain"),
            Medicine("Cipralex", 15.0, "Antidepressant for anxiety and depression"),
            Medicine("Calcui Forte", 12.0, "Calcium supplement for bone health"),
            Medicine("Nims (Nimesulide)", 7.0, "Pain reliever and anti-inflammatory"),
            Medicine("Augmentin", 10.0, "Antibiotic for bacterial infections"),
            Medicine("Disprin", 3.0, "Pain reliever and blood thinner"),
            Medicine("Metformin", 8.0, "Used for diabetes management"),
            Medicine("Omeprazole", 9.0, "Reduces stomach acid, used for heartburn"),
            Medicine("Loratadine", 6.0, "Allergy relief and antihistamine"),
            Medicine("Azithromycin", 14.0, "Broad-spectrum antibiotic"),
            Medicine("Hydroquin Forte", 13.0, "Iron and folic acid supplement"),
            Medicine("Xanax", 18.0, "Anti-anxiety medication"),
        ]

    def get_all_medicines(self):
        return self.medicines
