from BL.Doctor import Doctor
from BL.Nurse import Nurse
from BL.Pharmacist import Pharmacist

doctor = Doctor(
    name="Dr. Ali Khan",
    shift="Morning",
    address="Gulberg, Lahore",
    phone="0301-1234567",
    salary=150000,
    cnic="35201-1234567-8",
    specialization="Cardiology",
    experience=15,
    availability="9 AM - 3 PM",
    department="Cardiology"
)
nurse = Nurse(
    name="Nurse Sara",
    shift="Morning",
    address="Model Town, Lahore",
    phone="0312-9876543",
    salary=60000,
    cnic="35202-9876543-9",
    specialization="ICU",
    department="Intensive Care Unit"
)
pharmacist = Pharmacist(
    name="Pharmacist Muneeb",
    shift="Morning",
    address="PECHS, Karachi",
    phone="0345-2345678",
    salary=80000,
    cnic="42101-2345678-5",
    department="Pharmacy"
)