class Menu:
    def get_user_credentials(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username, password 

    def display_message(self, message):
        print(message)

    def main_menu(self):
        print("\n--- Hospital Management System ---")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice
    
    def display_doctors(self, doctors):
        if not doctors:
            print("No doctors are available at the moment.")
        else:
            print("\n--- Available Doctors ---")
            for doctor in doctors:
                print(doctor)

    def patient_menu(self):
        print("\n--- Patient Management Menu ---")
        print("1. View Doctors")
        print("2. Buy Medicine")
        print("3. View Bill")
        print("4. Log Out")
        choice = input("Enter your choice: ")
        return choice

    def get_patient_info(self):
        name = input("Enter patient's name: ")
        age = input("Enter patient's age: ")
        phone = input("Enter patient's phone number: ")
        cnic = input("Enter patient's CNIC: ")
        address = input("Enter patient's address: ")
        department = input("Enter patient's department: ")
        return name, age, phone, cnic, address, department

    def show_patients(self, patients):
        if not patients:
            print("No patients found.")
        else:
            print("\n--- Patients List ---")
            for patient in patients:
                print(f"Name: {patient.get_name()}, Age: {patient.get_age()}, Phone: {patient.get_phone()}")

    def doctor_menu(self):
        print("\n--- Doctor Management Menu ---")
        print("1. View Assigned Patients")
        print("2. Update Patient Records")
        print("3. View Schedule")
        print("4. Log Out")
        choice = input("Enter your choice: ")
        return choice


    def display_doctors(self, doctors):
        if not doctors:
            print("No doctors are available at the moment.")
        else:
            print("\n--- Available Doctors ---")
            for doctor in doctors:
                print(doctor)

    def nurse_menu(self):
        print("\n--- Nurse Menu ---")
        print("1. Assist Doctor")
        print("2. View Tasks : ")
        print("3. Perform Tasks : ")
        print("4. Log Out")
        return input("Enter your choice: ")
    
    def pharmacist_menu(self):
        print("\n--- Pharmacist Menu ---")
        print("1. View Medicine Stock")
        print("2. Dispense Medicine")
        print("3. Log Out")
        return input("Enter your choice: ")
    
    def get_patient_record_update(self):
        try:
            patient_index = int(input("Enter patient index to update: ")) - 1
            updated_condition = input("Enter updated condition: ")
            return patient_index, updated_condition
        except ValueError:
            print("Invalid input. Please enter numeric values for the patient index.")
            return -1, None
        
    def get_dispense_medicine_details(self):
        medicine_name = input("Enter the name of the medicine: ")
        try:
            quantity = int(input("Enter the quantity to dispense: "))
            return medicine_name, quantity
        except ValueError:
            print("Invalid input. Please enter a valid quantity as a number.")
            return None, None
        
    def get_medicine_purchase_details(self, medicines):
        print("\n--- Available Medicines ---")
        for idx, medicine in enumerate(medicines, start=1):
            print(f"{idx}. Name: {medicine.get_name()}, Price: {medicine.get_price()}, Description: {medicine.get_description()}")
        
        try:
            medicine_choice = int(input("Enter the number of the medicine to buy: ")) - 1
            quantity = int(input("Enter the quantity to purchase: "))
            return medicine_choice, quantity
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return None, None  