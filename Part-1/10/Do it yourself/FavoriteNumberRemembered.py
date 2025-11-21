from pathlib import Path
import json

path = Path('Favorite_Number.json')

if path.exists():
    contents = path.read_text()
    favorite_num = json.loads(contents)
    print(f"“I know your favorite number! It’s {favorite_num}")
else:
    favorite_num = int(input("What is your favorite number?\n-> "))
    path = Path('Favorite_Number.json')
    contents = json.dumps(favorite_num)
    path.write_text(contents)
    my_fav_num = json.loads(contents)
    print(f"We'll remember your favorite number: {my_fav_num}")





