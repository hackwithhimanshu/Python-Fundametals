river = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'ganga' : 'india',
}

for key, value in river.items():
    print(f"The {key.title()} runs through {value.title()}")
    