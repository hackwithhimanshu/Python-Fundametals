# requested_topics = 'mushrooms'

# if requested_topics != 'anchovies':
#     print("Hold the anchovies!")


# requested_toppings = ['mushrooms', 'green papers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green papers':
#         print("Sorry, we are out of gren paper")
#     else:
#         print(f"Adding {requested_topping}")

# print("\nFinish making your pizza")


# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
# else:
#     print("Are you sure you want plain pizza")

available_toppings = ['mushrooms', 'olives', 'green papers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinish making your pizza")