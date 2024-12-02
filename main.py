from DL.UserDL import UserDL
from BL.User import UserManager
from UI.UserMenu import Menu
from DL.PatientDL import PatientDL
from DL.DoctorDL import DoctorDL
from BL.Doctor import Doctor
from DL.MedicineDL import MedicineDL
from BL.patient import Patient

def main():
    user_dl = UserDL()
    user_logic = UserManager(user_dl)
    menu = Menu()
    doctor_dl = DoctorDL()
    medicine_dl = MedicineDL()
    patient = Patient()

    def initialize_doctors(doctor_dl):
        doctor_dl.add_doctor(
            name="Alice Smith",
            shift="Morning",
            address="123 Main St.",
            phone="123456789",
            salary="120000",
            cnic="12345-6789012-3",
            specialization="Cardiologist",
            experience="10 years",
            availability="9 AM - 1 PM",
            department="Cardiology"
        )

    initialize_doctors(doctor_dl)

    while True:
        choice = menu.main_menu()

        if choice == "1":
            username, password = menu.get_user_credentials()
            success = user_logic.sign_up(username, password)
            if success:
                menu.display_message("Sign-up successful! Welcome to the system.")
            else:
                print("Username already exists. Please try again.")

        elif choice == "2":
            username, password = menu.get_user_credentials()

            # Check if the user is a predefined doctor
            if user_dl.authenticate_predefined_role(username, password, "doctors"):
                menu.display_message(f"Welcome back, Dr. {username}!")
                while True:
                    doctor_choice = menu.doctor_menu()
                    if doctor_choice == "1":
                        print("Viewing patients...")
                        # Add functionality for viewing patients
                    elif doctor_choice == "2":
                        print("Updating patient records...")
                    elif doctor_choice == "3":
                        print("Viewing Schedule")
                    elif doctor_choice == "4":
                        print("Logging Out")
                        break
                    else:
                        menu.display_message("Invalid choice. Try again.")

            # Handle regular sign-in logic for other users
            else:
                user = user_logic.sign_in(username, password)
                if user:
                    menu.display_message(f"Welcome back, {username}!")
                    while True:
                        patient_choice = menu.patient_menu()
                        if patient_choice == "1":
                            doctors = doctor_dl.get_doctors()
                            menu.display_doctors(doctors)
                        elif patient_choice == "2":
                            patient.buy_medicine(medicine_dl)
                        elif patient_choice == "3":
                            patient.view_bill()
                        elif patient_choice == "4":
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    menu.display_message("Invalid username or password. Please try again.")

        elif choice == "3":
            menu.display_message("Exiting the system. Goodbye!")
            break

        else:
            menu.display_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
