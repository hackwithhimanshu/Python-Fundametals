prompt = "Please enter your age."
prompt += "type 'quit' as you finished\n-> "

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
         print("You have free entry")
        elif age >= 3 and age <= 12:
            print("Ticket charge 10$")
        else:
            print("Ticket charge 15$")

