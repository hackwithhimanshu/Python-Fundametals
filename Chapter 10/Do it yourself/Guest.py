from pathlib import Path

path = Path("guest.txt")

prompt = "Welcome to Name Dictionary\n"
prompt += "enter 'q' to exit\n"
prompt += "enter your name below\n->"


active_name = True


while True:
    name = input(prompt)
    if name.lower() == 'q':
      print("Thanks for input.\nExiting...")
      break
      
    else:
        with open(path, "a") as file:
          file.write(name + "\n")
        print(f"Hello, {name} is added to dictionary.")
       