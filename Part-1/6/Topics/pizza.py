pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print(f"Your ordered a {pizza['crust']}-crust pizza:" 
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")