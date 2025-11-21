my_foods = ['pizza', 'falafel', 'carrot cake', 'Chhole Bhature', 'Zini Dosa']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\n My friends favorite foods are: ")
print(friend_foods)

print("The first three items in the list are:")
for food in my_foods[:3]:
    print(food.title())

print("\nThree items from the middle of the lists are: ")
for food in my_foods[1:4]:
    print(food.title())

print("\nThe last three items in the list are: ")
for food in my_foods[-3:]:
    print(food.title())

