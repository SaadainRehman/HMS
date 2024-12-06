class User:
    def __init__(self, username, password, role):
        self._username = username  
        self._password = password  
        self._role = role  

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
    # Check if the username already exists in predefined roles
        for role, users in self.user_dl.predefined_roles.items():
            if username in users:
                print("Username is reserved for predefined roles. Please choose a different username.")
                return False

        # Check if the username already exists in the patients file
        if self.user_dl.get_user(username) is not None:
            print("Username already exists. Please choose a different username.")
            return False

        # Validate password
        if len(password) != 5 or not password.isdigit():
            print("Password must be exactly 5 digits. Please try again.")
            return False

        # Assign the "patient" role and create the new user
        new_user = User(username, password, "patient")
        self.user_dl.add_user(new_user)
        print("Sign-up successful! You are registered as a patient.")
        return True


    def sign_in(self, username, password):
        # print(f"DEBUG: Attempting sign-in for username: {username}")
        for role, users in self.user_dl.predefined_roles.items():
            # print(f"DEBUG: Checking role: {role}, Users: {users}")
            if username in users and users[username] == password:
                # print(f"DEBUG: Matched predefined role: {role}")
                return role  

        user = self.user_dl.get_user(username)
        if user:
            # print(f"DEBUG: Found patient record for username: {username}")
            if user.get_password() == password:
                # print(f"DEBUG: Matched patient password for username: {username}")
                return "patient"  # Return "patient" for patient users

        # print("DEBUG: Failed to authenticate user.")
        return None

