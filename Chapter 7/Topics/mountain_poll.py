responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n->")
    response = input("\nWhich mountain do you like to climb someday?\n->")

    responses[name] = response

    repeat = input("Would you like to let another person respond (yes/no)\n-> ")
    if repeat == 'no':
        polling_active = False

print('\n----Polling Results----')
for name, resopnse in responses.items():
    print(f"{name} like to climb {response}")