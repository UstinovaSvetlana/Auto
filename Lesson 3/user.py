class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print("Имя:", self.first_name)

    def print_last_name(self):
        print("Фамилия:", self.last_name)

    def print_full_name(self):
        print("Имя и фамилия:", self.first_name, self.last_name)

user = User("Sveta", "Ustinova")
user.print_first_name()
user.print_last_name()
user.print_full_name()