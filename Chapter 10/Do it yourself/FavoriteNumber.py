from pathlib import Path
import json

favorite_num = int(input("What is your favorite number?\n-> "))

path = Path('Favorite_Number.json')

contents = json.dumps(favorite_num)
path.write_text(contents)

my_fav_num = json.loads(contents)

print(f"We'll remember your favorite number: {my_fav_num}")