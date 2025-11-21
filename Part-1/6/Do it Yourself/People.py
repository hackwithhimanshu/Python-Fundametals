person1 = {
    'first_name' : 'Himanshu',
    'last_name' : 'Kumbhaj',
    'age' : 20,
    'city' : 'bhiali',
}

person2 = {
    'first name' : 'Akriti',
    'last name' : 'Dixit',
    'age' : 22,
    'city' : 'bhilai'
}

person3 = {
    'first name' : 'Uttam',
    'last name' : 'sinha',
    'age' : 21,
    'city' : 'raipur'
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key.title()} : {value}")
    print("-" * 20)
    
