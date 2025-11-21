# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('adrian', 'nobert')
# print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jim', 'caromenda', age=23)
print(musician)