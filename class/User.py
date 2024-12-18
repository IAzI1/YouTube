class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.__nickname = nickname
        self.__password = hash(password)
        self.__age = age

    @property
    def nickname(self):
        return self.__nickname

    @property
    def password(self):
        return self.__password

    @property
    def age(self):
        return self.__age

user = User('aziz', 1212313, 15)
print(user.password)
