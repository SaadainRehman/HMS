from DL.UserDL import UserDL
from BL.User import UserManager
from UI.UserMenu import Menu
from DL.MedicineDL import MedicineDL
from BL.patient import Patient
from InitialData.data import nurse, pharmacist
from BL.Doctor import Doctor

def main():
    user_dl = UserDL()
    user_logic = UserManager(user_dl)
    menu = Menu()
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
   

    while True:
        # Display the main menu and get user choice
        choice = menu.main_menu()

        if choice == "1":  # Sign-up
            username, password = menu.get_user_credentials()

            # Perform validation and sign-up
            success = user_logic.sign_up(username, password)
            if success:
                menu.display_message("Sign-up successful! Welcome to the system.")
            else:
                menu.display_message("Sign-up failed. Please try again.")

        elif choice == "2":  # Sign-in
            username, password = menu.get_user_credentials()

            # Authenticate predefined roles first
            for role in ["doctors", "nurses", "pharmacists"]:
                if user_dl.authenticate_predefined_role(username, password, role):
                    menu.display_message(f"Welcome back, {role[:-1].capitalize()} {username}!")
                    
                    # Role-specific menus
                    if role == "doctors":
                        while True:
                            doctor_choice = menu.doctor_menu()
                            if doctor_choice == "1":
                                print(doctor.view_assigned_patients())
                            elif doctor_choice == "2":
                                patient_index, updated_condition = menu.get_patient_record_update()
                                if patient_index == -1 or updated_condition is None:
                                    print("Failed to update patient records due to invalid input.")
                                else:
                                    print(doctor.update_patient_records(patient_index, updated_condition))
                            elif doctor_choice == "3":
                                print(doctor.view_schedule())
                            elif doctor_choice == "4":
                                print("Logging out...")
                                break
                            else:
                                menu.display_message("Invalid choice. Try again.")

                    elif role == "pharmacists":
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

                    elif role == "nurses":
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
                    break  # Exit role check after matching role

            else:  # If not a predefined role, check patient login
                user = user_logic.sign_in(username, password)
                if user:
                    menu.display_message(f"Welcome back, {username}!")
                    while True:
                        patient_choice = menu.patient_menu()
                        if patient_choice == "1":
                            doctor = patient.view_doctors()
                            # menu.display_doctors(doctors)
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

        elif choice == "3":  # Exit
            menu.display_message("Exiting the system. Goodbye!")
            break

        else:  # Invalid menu choice
            menu.display_message("Invalid choice. Please try again.")

main()
