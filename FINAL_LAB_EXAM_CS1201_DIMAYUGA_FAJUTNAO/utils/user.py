class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wins = 0

    def __repr__(self):
        return f"{self.username},{self.password},{self.wins}"

    @classmethod
    def from_string(cls, user_data):
        username, password, wins = user_data.split(',')
        user = cls(username, password)
        user.wins = int(wins)
        return user
