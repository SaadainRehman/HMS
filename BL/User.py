class User:
    def __init__(self, username, password, role):
        self._username = username  # Protected
        self._password = password  # Protected
        self._role = role  # Protected

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_role(self):
        return self._role
    
    def set_role(self):
        self._role = "patient"

    def __str__(self):
        return f"Username: {self._username}, Role: {self._role}"
    

class UserManager:
    def __init__(self, user_dl):
        self.user_dl = user_dl

    def sign_up(self, username, password):
        if len(password) == 5 and password.isdigit():
            if self.user_dl.get_user(username) is None:
                new_user = User(username, password, role="patient")
                self.user_dl.add_user(new_user)
                return True
            else:
                print("Username already exists.")
                return False
        else:
            print("Password must be exactly 5 digits.")
            return False

    def sign_in(self, username, password):
        user = self.user_dl.get_user(username)
        if user and user.get_password() == password:
            role = user.get_role()

            for predefined_role, users in self.user_dl.predefined_roles.items():
                if username in users:
                    user._role = predefined_role
                    break

            return user
        return None


