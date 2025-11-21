
favorite_place = {}

favorite_place_active = True 

while favorite_place_active:
    name = input("What is your name?\n-> ")
    vacation = input("if you could visit one place in the world where would you go?\n-> ")

    favorite_place[name] = vacation

    next_person = input("----Do you wanna let another person give input (yes/no)----")
    if next_person == 'no':
        favorite_place_active = False


print("\n---Poll result---")

for name, vacation in favorite_place.items():
    print(f"{name} like to visit {vacation}")