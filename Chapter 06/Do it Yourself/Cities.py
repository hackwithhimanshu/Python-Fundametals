cities = {        
    'raipur' : {
        'country' : 'india',
        'population' : '2 crore',
        'fact' : 'capital of india',
    },
    'bhilai' : {
        'country' : 'india',
        'population' : '1 crore',
        'fact' : 'student hub'

    },
    'dhamtari' : {
        'country' : 'india',
        'population' : '50 lakh',
        'fact' : 'gangrel river'
    }
    }

for city, info in cities.items():
    print(city.title())
    for key, value in info.items():
        print(f"{key.title()} : {value.title()}")
    print("-" * 20)