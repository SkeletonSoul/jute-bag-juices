class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User created")

    def introduce_self(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}")

    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}, email='{self.email})"
    def __str__(self):
        return self.__repr__()


john = User('john', 'john doe', 'john@gmail.com')
print(john)
john.introduce_self('Rama')

jane = User('jane', 'jane doe', 'jane@gmail.com')
mary = User('mary', 'mary doe', 'mary@gmail.com')
alice = User('alice', 'alice doe', 'alice@gmail.com')

users = [john, jane, mary, alice]
print(users)

class UserDatabase:
    def __init__(self):
        self.users = []
        
    def insert(self, user):
        pass

    def find(self, user):
        pass

    def update(self, user):
        pass

    def list(self, user):
        pass
