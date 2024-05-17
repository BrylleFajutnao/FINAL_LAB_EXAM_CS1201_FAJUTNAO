
class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return False
        self.users[username] = User(username, password)
        return True

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("Login successful.")
            return True
        print("Invalid username or password.")
        return False

    def logout(self):
        print("Logged out successfully.")
        return True