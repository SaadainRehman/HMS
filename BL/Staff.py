class Staff:
    def __init__(self, name, shift, address, phone, salary, cnic):
        self._name = name  # Protected
        self._shift = shift  # Protected
        self._address = address  # Protected
        self._phone = phone  # Protected
        self._salary = salary  # Protected
        self._cnic = cnic  # Protected

    def __str__(self):
        return f"Name: {self._name}, Shift: {self._shift}, Address: {self._address}, Phone: {self._phone}, Salary: {self._salary}, CNIC: {self._cnic}"
