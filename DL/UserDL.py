from BL.User import User
class UserDL:
    def __init__(self, predefined_roles_file="predefined_roles.txt", patients_file="patients.txt"):
        self.predefined_roles_file = predefined_roles_file
        self.patients_file = patients_file
        self.predefined_roles = self.load_predefined_roles()
        self.users = self.load_patients()

    def load_predefined_roles(self):
        roles = {"doctors": {}, "nurses": {}, "pharmacists": {}}
        try:
            with open(self.predefined_roles_file, "r") as file:
                for line in file:
                    role, username, password = line.strip().split(",")
                    if role in roles:
                        roles[role][username] = password
        except FileNotFoundError:
            # Initialize with predefined roles if file doesn't exist
            roles = {
                "doctors": {"Ali": "78978", "Saqlain": "78676", "Ahmad": "11111"},
                "nurses": {"waqar": "24763", "hassan": "99999"},
                "pharmacists": {"muneeb": "12871", "shehzad": "23487"},
            }
            self.save_predefined_roles(roles)
        return roles

    def save_predefined_roles(self, roles):
        with open(self.predefined_roles_file, "w") as file:
            for role, users in roles.items():
                for username, password in users.items():
                    file.write(f"{role},{username},{password}\n")

    def load_patients(self):
        patients = []
        try:
            with open(self.patients_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    patients.append(User(username, password, "patient"))
        except FileNotFoundError:
            pass
        return patients

    def save_patients(self):
        with open(self.patients_file, "w") as file:
            for user in self.users:
                file.write(f"{user.get_username()},{user.get_password()}\n")

    def add_user(self, user):
        self.users.append(user)
        self.save_patients()

    def get_user(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user
        return None

    def authenticate_predefined_role(self, username, password, role):
        role_dict = self.predefined_roles.get(role)
        if role_dict:
            return role_dict.get(username) == password
        return False
    
