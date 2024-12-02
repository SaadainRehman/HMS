class UserDL:
    def __init__(self):
        self.users = []  
        self.predefined_roles = {
            "doctors": {"Ali Naeem": "789789", "Saqlain": "786786"},
            "nurses": {"shaheer": "6969", "hassaan": "9999"},
            "pharmacists": {"muneeb": "pharma", "hassan": "pharma2"},
        }

    def add_user(self, user):
        self.users.append(user)

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

