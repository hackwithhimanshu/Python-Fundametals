# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect
# all the names that are entered, and then write these names to a file called
# guest_book.txt. Make sure each entry appears on a new line in the file.


from pathlib import Path

path = Path("guest_list.txt")

prompt = "Welcome to guest entry"
prompt = "press 'q' to quit"
prompt = "Enter your name\n-> "

gues_active = True



while True:
    name = input(prompt)
    
    if name == 'q':
        print("Guest Book exiting....")
        break
    else:
        with open(path, "a") as file:
            file.write(name + "\n")
            print(f"Thanks for entering {name}")
     
