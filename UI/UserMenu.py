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

    # def patient_menu(self):
    #     print("\n--- Patient Management Menu ---")
    #     print("1. Add Patient")
    #     print("2. View All Patients")
    #     print("3. Update Patient Information")
    #     print("4. Delete Patient")
    #     print("5. Log Out")
    #     choice = input("Enter your choice: ")
    #     return choice

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
