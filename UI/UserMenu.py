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
        print("2. Check Vitals")
        print("3. Administer Medicine")
        print("4. Log Out")
        return input("Enter your choice: ")