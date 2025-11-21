favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phill' : 'python',
}

student = ['jen', 'edward', 'jimmy', 'michel']

for person in student:
    if person in favorite_languages:
        print(f"{person} thankyou for taking the poll")
    if person not in favorite_languages:
        print(f"{person} we invite you to take the poll")
        