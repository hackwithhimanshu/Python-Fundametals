from pathlib import Path

path = Path('10/Topics/pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Enter your brithday in ddmmyy: ")

if birthday in pi_string:
    print("Your birthday appears in frist million digits of pi")
else:
    print("Your birthday does not appears in frist million digits of pi")

