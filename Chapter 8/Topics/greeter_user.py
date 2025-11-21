def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
    
usernames = ['tanjiro', 'zenitsu', 'inosuke']
greet_user(usernames)