# app/user.py

class User:
    users = {}

    @staticmethod
    def register(username, password):
        if username in User.users:
            return False
        User.users[username] = password
        return True

    @staticmethod
    def login(username, password):
        if username not in User.users:
            return False
        return User.users[username] == password
