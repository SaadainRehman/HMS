# class UserDL:
#     def __init__(self):
#         self.users = []  
#         self.predefined_roles = { "doctors": ["Ali Naeem": "789789", "Saqlain" : "786786"],
#             "nurses": ["nurse1", "nurse2"],
#             "pharmacists": ["pharma1", "pharma2"],
#         }

#     def add_user(self, user):
#         self.users.append(user)

#     def get_user(self, username):
#         for user in self.users:
#             if user.get_username() == username:
#                 return user
#         return None
    
#     def authenticate_predefined_role(self, username, password, role):
#         role_dict = self.predefined_roles.get(role, {})
#         return role_dict.get(username) == password

#     # def is_predefined_role(self, username, role):
#     #     role_dict = self.predefined_roles.get(role, {})
#     #     return username in role_dict

#     # def authenticate_predefined_role(self, username, password, role):
#     #     role_dict = self.predefined_roles.get(role, {})
#     #     return role_dict.get(username) == password


class UserDL:
    def __init__(self):
        self.users = []  
        self.predefined_roles = {
            "doctors": {"Ali Naeem": "789789", "Saqlain": "786786"},
            "nurses": {"nurse1": "nursepass1", "nurse2": "nursepass2"},
            "pharmacists": {"pharma1": "pharmapass1", "pharma2": "pharmapass2"},
        }

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user
        return None
    
    def authenticate_predefined_role(self, username, password, role):
        # Check if the role exists in predefined roles
        role_dict = self.predefined_roles.get(role)
        if role_dict:
            return role_dict.get(username) == password
        return False
