class Library:
    def __init__(self):
        self.user_records = []  # [user.object1, user.object2]
        self.books_available = {}  # {author: [book1, book2, book3]
        self.rented_books = {}  # {username: {book: days_to_return}

    def add_user(self, user: object):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user: object):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        if user.username in self.rented_books:
            del self.rented_books[user.username]  # check again

    def change_username(self, user_id: int, new_username: str):
        # user_records update:
        for object in self.user_records:
            if object.user_id == user_id:
                if object.username == new_username:
                    return "Please check again the provided username - \
it should be different than the username used so far!"
                # rented_books update:
                if object.username in self.rented_books:
                    # change old username with new username
                    self.rented_books[new_username] = self.rented_books.pop(object.username)
                # user_records update:
                object.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"
