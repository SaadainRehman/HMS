class Patient:
    def __init__(self, name=None, age=None, phone=None, cnic=None, address=None, department=None):
        self._name = name
        self._age = age
        self._phone = phone
        self._cnic = cnic
        self._address = address
        self._department = department

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age

    def get_phone(self):
        return self._phone

    def get_cnic(self):
        return self._cnic

    def get_address(self):
        return self._address
    
    def get_department(self):
        return self._department

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_phone(self, phone):
        self._phone = phone

    def set_cnic(self, cnic):
        self._cnic = cnic

    def set_address(self, address):
        self._address = address

    def set_department(self, department):
        self._department = department

    def view_doctors(self):
        print("Viewing available doctors...")

    def buy_medicine(self, medicine_dl):
        medicines = medicine_dl.get_all_medicines()
        print("\n--- Available Medicines ---")
        for medicine in medicines:
            print(f"Name: {medicine.get_name()}, Price: {medicine.get_price()}, Description: {medicine.get_description()}")

    def view_bill(self):
        print("Viewing bill...")