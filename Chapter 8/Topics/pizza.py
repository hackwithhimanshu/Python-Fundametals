# def make_pizza(*toppings):
#     print("\nMake a pizza with the following toppings:-")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('loaded Cheese')
# make_pizza('Pineapple', 'cheese', 'corn', 'extra chilli flakes')

def make_pizza(size, *toppings):
    print(f"\nMaking a {size} pizza with following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'loaded Cheese')
make_pizza(12, 'Pineapple', 'cheese', 'corn', 'extra chilli flakes')
