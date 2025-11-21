class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}\nWelcome to Python.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.login_attempts} no. of login attempts performed")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login reset")
        

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

user_one.increment_login_attempts()
user_one.increment_login_attempts() 
user_one.increment_login_attempts()
user_one.increment_login_attempts()

user_one.reset_login_attempts()



