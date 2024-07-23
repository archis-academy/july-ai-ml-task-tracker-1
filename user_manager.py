import re
from user import User
class UserManager:

    def __init__(self): 
        self.users = {}  # key value {username,user_object}
        self.next_id = 1  

    def user_register(self, username, password, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return("Invalid email address. Example: martymcfly@gmail.com")
        
        if not re.match(r"^[a-zA-Z0-9_]{3,}$", username):
            return("Invalid username. It must be at least 3 characters long and contain only letters, numbers, and underscores.")
        
        if len(password) < 6:
            return("Password must be at least 6 characters long.")
        
        if email in self.users:
            return("Email already exists.")

        if username in self.users:
            return("Username already exists. Please choose a different username.")
    
        user_id = self.next_id
        self.next_id += 1  

        new_user = User(email, username, password, user_id)
        self.users[username] = new_user

        print(f"User registered successfully with ID {user_id}!")
