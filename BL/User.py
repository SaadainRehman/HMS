class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self, user_dl):
        self.user_dl = user_dl 

    def sign_up(self, username, password):
        if self.user_dl.is_valid(username):
            new_user = User(username, password)
            self.user_dl.add_user(new_user)
            return True
        return None

    def sign_in(self, username, password):
        user = self.user_dl.get_user(username)
        if user and user.password == password:
            return user
        return None
