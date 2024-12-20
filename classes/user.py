class User:

    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname.lower()
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname

