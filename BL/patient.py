class Patient:
    def __init__(self, name=None, age=None, phone=None, cnic=None, address=None, department=None):
        self._name = name
        self._age = age
        self._phone = phone
        self._cnic = cnic
        self._address = address
        self._department = department
        self.cart = []  # To store medicines and quantities for billing

    # Getter and Setter methods
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

    # Function to view doctors
    def view_doctors(self):
        doctors = [
            {"name": "Dr. Ali Khan", "specialization": "Cardiologist", "experience": "15 years"},
            {"name": "Dr. Maria Ahmed", "specialization": "Dermatologist", "experience": "10 years"},
            {"name": "Dr. Asad Baig", "specialization": "Neurologist", "experience": "12 years"},
            {"name": "Dr. Farah Zafar", "specialization": "Pediatrician", "experience": "8 years"},
            {"name": "Dr. Usman Tariq", "specialization": "Orthopedic Surgeon", "experience": "18 years"},
        ]
        print("Available doctors:")
        for idx, doctor in enumerate(doctors, start=1):
            print(f"{idx}. {doctor['name']} - {doctor['specialization']} ({doctor['experience']} experience)")
        return doctors

    # Function to buy medicines
    def buy_medicine(self, medicine_dl):
        medicines = medicine_dl.get_all_medicines()
        print("\n--- Available Medicines ---")
        for medicine in medicines:
            print(f"Name: {medicine.get_name()}, Price: {medicine.get_price()}, Description: {medicine.get_description()}")

        while True:
            medicine_name = input("\nEnter the name of the medicine to buy (or type 'done' to finish): ").strip()
            if medicine_name.lower() == "done":
                break

            # selected_medicine = next((m for m in medicines if m.get_name().lower() == medicine_name.lower()), None)
            selected_medicine = None 
            for medicine in medicines:
                if medicine.get_name().lower() == medicine_name.lower():
                    selected_medicine = medicine 
                    break  

            if not selected_medicine:

                print("Medicine not found. Please try again.")
                continue

            try:
                quantity = int(input(f"Enter the quantity of {selected_medicine.get_name()}: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a numeric value for quantity.")
                continue

            # Add the medicine and quantity to the cart
            self.cart.append({"medicine": selected_medicine, "quantity": quantity})
            print(f"Added {quantity} of {selected_medicine.get_name()} to your cart.")

        print("\nMedicine purchasing completed.")

    # Function to view the bill
    def view_bill(self):
        print("\n--- Bill Summary ---")
        total_amount = 0
        for item in self.cart:
            medicine = item["medicine"]
            quantity = item["quantity"]
            cost = medicine.get_price() * quantity
            total_amount += cost
            print(f"{medicine.get_name()} x {quantity} = ${cost:.2f}")
        print(f"Total Amount: ${total_amount:.2f}")
