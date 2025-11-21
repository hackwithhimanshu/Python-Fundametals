from pathlib import Path

path = Path("10/Topics/pi_digits.txt")

contents = path.read_text()


for content in contents.splitlines():
    print(content)