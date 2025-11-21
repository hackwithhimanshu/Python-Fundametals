from pathlib import Path
import json 

path = Path('Favorite_Number.json')

contents = path.read_text()

favorite_num = json.loads(contents)
print(f"“I know your favorite number! It’s {favorite_num}")

