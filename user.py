class User:

    def __init__(self, email, username, password, id ):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.shared_tasks = {}

