class Patient:
    def __init__(self, name, age, phone, cnic, address, department):
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
