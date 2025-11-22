# # from pathlib import Path
# # import json

# # username = input("What is your name?\n-> ")

# # path = Path("username.json")
# # contents = json.dumps(username)
# # path.write_text(contents)

# # print(f"We'll remember you when you come back {username}!")


# from pathlib import Path
# import json

# path = Path("username.json")

# def greet_user():

#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}")
#     else:
#         username = input("What is your name?\n-> ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}")

# greet_user()


from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("What is your name?\n-> ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

    

def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

greet_user()
