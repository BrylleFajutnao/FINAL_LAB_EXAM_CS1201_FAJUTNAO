from utils.user import User


class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open('user.txt', 'r') as file:
                for line in file:
                    user = User.from_string(line.strip())
                    self.users[user.username] = user
        except FileNotFoundError:
            pass
            

    def save_users(self):
        with open('user.txt', 'w') as file:
            for user in self.users.values():
                file.write(f"{user}\n")

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return False
        self.users[username] = User(username, password)
        self.save_users()
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
