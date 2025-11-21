users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },

    'davinci' : {
        'first' : 'Scarlet',
        'last' : 'drownzer',
        'location' : 'london',
    },

    'leonardo' : {
        'first' : 'sherlock',
        'last' : 'homes',
        'location' : 'paris',
    }
}

for name, data in users.items():
    print(name.title())
    for key, value in data.items():
        print(f"{key.title()} : {value.title()}")
    print("-" * 20)