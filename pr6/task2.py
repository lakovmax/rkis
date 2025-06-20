class User:
    __login = ''
    __password = ''

    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    def __str__(self):
        return f"Login: {self.__login}, Password: {self.__password}"


users = [User("", "1234321"),
         User("Maxim", "15263748"),
         User("Oleg", "okak"),
         User("Michael", "1234"),
         User("Kirill", "qwerty")]

login = input("Введите логин: ")
password = input("Введите пароль: ")
for user in users:
    if user.login == login and user.password == password:
        print(user)