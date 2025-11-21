myfavpizzas = ['veg loaded pizza', 'cheese corn pizza', 'paneer tandoori pizza', 'marghereta pizza', 'farm house pizza',]
friendpizzas = myfavpizzas[:]

myfavpizzas.append('social house pizza')
friendpizzas.append('lapinoz pizza')

print("My favorite pizzas are: ")
for myfavpizza in myfavpizzas[:]:
    print(myfavpizza.title())

print("\nMy friends fav pizza's are: ")
for friendpizza in friendpizzas[:]:
    print(friendpizza.title())