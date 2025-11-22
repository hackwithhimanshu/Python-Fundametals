class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}\nWelcome to Python.")

user_one = User('himanshu', 'kumbhaj')
user_two = User('Akrit', 'Dixit')
user_three = User('Samdarshi', 'Parihar')

user_one.describe_user()
user_one.greet_user()
print("*"*10)
user_two.describe_user()
user_two.greet_user()
print("*"*10)

user_three.describe_user()
user_three.greet_user()
print("*"*10)


