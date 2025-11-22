from pathlib import Path

path = Path("commonword.txt")

contents = path.read_text(encoding="utf-8")

# print(len(contents))

print(contents.count('the '))

print(contents.lower().count('the '))


