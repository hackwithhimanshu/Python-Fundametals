
def print_models(unprinted_desings, completed_models):
    while unprinted_desings:
        current_design = unprinted_desings.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nFollowing models are completed:-")
    for completed_model in completed_models:
        print(completed_model)