import json
import bcrypt
import argparse
import os

class UserAuthentication:
    def __init__(self, user_db='users.json'):
        self.user_db = user_db
        self.load_users()

    def load_users(self):
        """Load users from the JSON file."""
        if os.path.exists(self.user_db):
            with open(self.user_db, 'r') as db_file:
                self.users = json.load(db_file)
        else:
            self.users = {}

    def save_users(self):
        """Save users to the JSON file."""
        with open(self.user_db, 'w') as db_file:
            json.dump(self.users, db_file)

    def register(self, username, password):
        """Register a new user."""
        if username in self.users:
            print("Username already exists.")
            return False
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.users[username] = hashed.decode('utf-8')
        self.save_users()
        print("User registered successfully.")
        return True

    def login(self, username, password):
        """Log in a user."""
        if username not in self.users:
            print("Username not found.")
            return False
        
        if bcrypt.checkpw(password.encode('utf-8'), self.users[username].encode('utf-8')):
            print("Login successful.")
            return True
        else:
            print("Invalid password.")
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='User Authentication System.')
    parser.add_argument('action', choices=['register', 'login'], help='Action to perform: register or login')
    parser.add_argument('username', type=str, help='Username for the account')
    parser.add_argument('password', type=str, help='Password for the account')

    args = parser.parse_args()

    auth_system = UserAuthentication()

    if args.action == 'register':
        auth_system.register(args.username, args.password)
    elif args.action == 'login':
        auth_system.login(args.username, args.password)
