pet_1 = {
    'pet' : 'dog',
    'pet name' : 'jim',
    'owner' : 'john',
}
pet_2 = {
    'pet' : 'cat',
    'pet name' : 'miki',
    'owner' : 'michel',
}
pet_3 = {
    'pet' : 'parrot',
    'pet name' : 'nametade',
    'owner' : 'leonardo',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key} : {value}")
    print("-" * 20)
