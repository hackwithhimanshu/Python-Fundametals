def sandwiches_stuff(*add_stuffs):
    print("What would you like in your sandwich:- ")
    for add_stuff in add_stuffs:
        print(f"-{add_stuff}")

sandwiches_stuff('pattie', 'cheese', 'veg loaded')