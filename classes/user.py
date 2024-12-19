class User:

    def __init__(self, nickname: str, password, age: int):
        self.__nickname = nickname.lower()
        self.__password = hash(password)
        self.__age = age

    @property
    def nickname(self):
        return self.__nickname

    @property
    def password(self):
        return self.__password

    def __str__(self):
        return self.__nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.__nickname == other.__nickname

