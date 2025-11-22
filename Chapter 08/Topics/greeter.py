# def greeter_user():
#     '''Display a simple greeting.'''
#     print("Hello!")

# greeter_user()

# def greeter_user(username):
#     print(f"Hello, {username.title()}")

# greeter_user('Himanshu')

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# print("\nPlease tell me your name.")
# f_name = input("first name: ")
# l_name = input("last name: ")

# formatted_name = get_formatted_name(f_name, l_name)
# print(f"\nHello, {formatted_name}!")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

while True:
    print("\nEnter your name.")
    print("(enter 'q' any time to quit)")

    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
