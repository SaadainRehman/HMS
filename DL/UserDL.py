class Userdl:
    def __init__(self):
        self.Users = []  

    def is_valid(self, username):
        for existing_user in self.Users:
            if existing_user.username == username:
                return False
        return True

    def add_user(self, user):
        self.Users.append(user)

    def get_user(self, username):
        for user in self.Users:
            if user.username == username:
                return user
        return None
