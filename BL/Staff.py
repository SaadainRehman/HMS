from abc import ABC , abstractmethod

class Person(ABC):
    @abstractmethod
    def show_details(self):
        pass

class Staff(Person):
    def __init__(self, name, shift, address, phone, salary, cnic):
        self._name = name  
        self._shift = shift 
        self._address = address
        self._phone = phone 
        self._salary = salary
        self._cnic = cnic  

    def show_details(self):
         return f"Name: {self._name}, Shift: {self._shift}, Address: {self._address}, Phone: {self._phone}, Salary: {self._salary}, CNIC: {self._cnic}"
    
    def __str__(self):
        return f"Name: {self._name}, Shift: {self._shift}, Address: {self._address}, Phone: {self._phone}, Salary: {self._salary}, CNIC: {self._cnic}"
