class UserDL:
    def __init__(self):
        self.users = []  
        self.predefined_roles = {
            "doctors": {"Ali Naeem": "789789", "Saqlain": "786786"},
            "nurses": {"shaheer": "6969", "hassaan": "9999"},
            "pharmacists": {"pharma1": "pharmapass1", "pharma2": "pharmapass2"},
        }

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user
        return None
    
    # def authenticate_predefined_role(self, username, password, role):
    #     # Check if the role exists in predefined roles
    #     role_dict = self.predefined_roles.get(role)
    #     if role_dict:
    #         return role_dict.get(username) == password
    #     return False

    def authenticate_predefined_role(self, username, password, role):
        role_dict = self.predefined_roles.get(role)
        print(f"Authenticating: role={role}, username={username}, password={password}")
        print(f"Role data: {role_dict}")
        if role_dict:
            print(f"Password match: {role_dict.get(username) == password}")
            return role_dict.get(username) == password
        return False

