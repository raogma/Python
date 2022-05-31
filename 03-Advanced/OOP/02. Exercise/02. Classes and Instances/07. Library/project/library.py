class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: object):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user: object):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        for username in self.rented_books:
            if username == user.username:
                del self.rented_books[username]
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        for object in self.user_records:
            if object.user_id == user_id:
                if object.username == new_username:
                    return f"Please check again the provided username - \
it should be different than the username used so far!"
                # Change his username in the rented_books dictionary as well (if present).
                for user in self.rented_books:
                    if user == object.username:
                        self.rented_books[new_username] = self.rented_books.pop(user) ##!!!!!
                # Change his username in the rented_books dictionary as well (if present).
                object.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {object.user_id}"
        return f"There is no user with id = {user_id}!"

