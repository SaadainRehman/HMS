from DL.UserDL import UserDL
from BL.User import UserManager
from UI.UserMenu import Menu
from DL.PatientDL import PatientDL
from DL.DoctorDL import DoctorDL
from BL.Doctor import Doctor
from DL.MedicineDL import MedicineDL
from BL.patient import Patient
from DL.Nurse import NurseDL
from DL.PharmacistDL import PharmacistDL
from BL.Nurse import Nurse
from BL.Pharmacist import Pharmacist

def main():
    user_dl = UserDL()
    user_logic = UserManager(user_dl)
    menu = Menu()
    doctor_dl = DoctorDL()
    medicine_dl = MedicineDL()
    patient = Patient()
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

    while True:
        choice = menu.main_menu()

        if choice == "1":
            username, password = menu.get_user_credentials()
            
            if len(password) != 5 or not password.isdigit():
                menu.display_message("Password must be exactly 5 digits. Please try again.")
            elif user_logic.user_dl.get_user(username) is not None:
                menu.display_message("Username already exists. Please choose a different username.")
            else:
                success = user_logic.sign_up(username, password)
                if success:
                    menu.display_message("Sign-up successful! Welcome to the system.")
                    
        elif choice == "2":
            username, password = menu.get_user_credentials()
            if user_logic.sign_in(username, password):
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


            # Authenticate Doctor
            elif user_dl.authenticate_predefined_role(username, password, "doctors"):
                menu.display_message(f"Welcome back, Dr. {username}!")
                while True:
                    doctor_choice = menu.doctor_menu()
                    if doctor_choice == "1":
                        print(doctor.view_assigned_patients())
                    elif doctor_choice == "2":
                        patient_index, updated_condition = menu.get_patient_record_update()  # Get input via UserMenu
                        if patient_index == -1 or updated_condition is None:
                            print("Failed to update patient records due to invalid input.")
                        else:
                            print(doctor.update_patient_records(patient_index, updated_condition))  # Update records
                    elif doctor_choice == "3":
                        print(doctor.view_schedule())
                    elif doctor_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        menu.display_message("Invalid choice. Try again.")

            elif user_dl.authenticate_predefined_role(username, password, "pharmacists"):
                menu.display_message(f"Welcome back, Pharmacist {username}!")
                while True:
                    pharmacist_choice = menu.pharmacist_menu()
                    if pharmacist_choice == "1":
                        print(pharmacist.view_medicine_stock())
                    elif pharmacist_choice == "2":
                        medicine_name, quantity = menu.get_dispense_medicine_details() 
                        if medicine_name is None or quantity is None:
                            print("Failed to dispense medicine due to invalid input.")
                        else:
                            print(pharmacist.dispense_medicine(medicine_name, quantity))
                    elif pharmacist_choice == "3":
                        print("Logging out...")
                        break
                    else:
                        menu.display_message("Invalid choice. Try again.")

            elif user_dl.authenticate_predefined_role(username, password, "nurses"):
                menu.display_message(f"Welcome back, Nurse {username}!")
                while True:
                    nurse_choice = menu.nurse_menu()
                    if nurse_choice == "1":
                        print(nurse.assist_doctor())
                    elif nurse_choice == "2":
                        print(nurse.view_tasks())
                    elif nurse_choice == "3":
                        task_index = nurse.task_index()
                        if task_index == -1:
                            print("Invalid input. Please enter a valid task number.")
                        else:
                            print(nurse.perform_task(task_index)) 
                    elif nurse_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        menu.display_message("Invalid choice. Try again.")    
            else:
                menu.display_message("Invalid username or password. Please try again.")

        elif choice == "3":
            menu.display_message("Exiting the system. Goodbye!")
            break

        else:
            menu.display_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
