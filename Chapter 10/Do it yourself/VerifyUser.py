from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        try:
            username = json.loads(contents)
            return username
        except json.JSONDecodeError:
            return None
    else:
        return None

def get_new_username(path):
    username = input("What is your name?\n-> ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    path = Path("username_2.json")
    username = get_stored_username(path)
    
    if username:
        check_user = input(f"Are you {username}!  (yes/no)\n-> ")
        if check_user == 'yes':
            print(f"Welcome back, {username}")

        else:
            username = get_new_username(path)
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

# def check_user():
#     ask_user = input(f"Are you {get_stored_username}")
#     if ask_user == True:
#         greet_user()
#     else:
#         get_new_username()

greet_user()
# check_user()
