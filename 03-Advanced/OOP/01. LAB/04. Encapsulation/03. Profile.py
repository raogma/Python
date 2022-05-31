class Profile:
    def __init__(self, username, password):
        self.__username = username
        if len(self.__username) < 5 or len(self.__username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__password = password
        hasUpper = False
        hasDigit = False
        for ch in self.__password:
            if ch.isupper():
                hasUpper = True
            if ch.isdigit():
                hasDigit = True
        if len(self.__password) < 8 or not hasUpper or not hasDigit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {len(self.__password) * "*"}'


profile_with_invalid_username = Profile('Too_long_username', 'Any')