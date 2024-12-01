from DL.UserDL import Userdl
from BL.User import UserManager
from UI.UserMenu import Menu
from DL.PatientDL import PatientDL

def main():
    user_dl = Userdl()
    user_logic = UserManager(user_dl)
    menu = Menu()
    patientdl = PatientDL()

    while True:
        choice = menu.main_menu()

        if choice == "1": 
            username, password = menu.get_user_credentials()
            success = user_logic.sign_up(username, password)
            if success: 
                menu.display_message("Sign-up successful! Welcome to the system.") 
            else:
                print ("Username already exists. Please try again.")

        elif choice == "2": 
            username, password = menu.get_user_credentials()
            user = user_logic.sign_in(username, password)
            if user:
                menu.display_message(f"Welcome back, {username}!")
                menu.patient_menu()
                choice1 = choice
                if choice1 == "1":
                    print("These dr availible right now")
                elif choice1 == "2":
                    print("These medicine availible right now")
                elif choice1 == "3":
                    print("Your bill is 100")
                else:
                    print("Logging out")
                    break
            else: 
                menu.display_message("Invalid username or password. Please try again.")

        elif choice == "3": 
            menu.display_message("Exiting the system. Goodbye!")
            break

        else:
            menu.display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()