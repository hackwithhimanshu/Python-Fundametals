# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phill' : 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}")


favorite_languages = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")