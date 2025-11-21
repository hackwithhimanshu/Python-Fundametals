# unprinted_designs = ['naruto keychan', 'phonecase', 'spiderman logo']
# completed_designs = []

# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print(f"Print Model: {current_designs}")
#     completed_designs.append(current_designs)

# print("\nFollowing models are completed:-")
# for completed_design in completed_designs:
#     print(completed_design)


def print_models(unprinted_desings, completed_models):
    while unprinted_desings:
        current_design = unprinted_desings.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nFollowing models are completed:-")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['naruto keychan', 'phonecase', 'spiderman logo']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)