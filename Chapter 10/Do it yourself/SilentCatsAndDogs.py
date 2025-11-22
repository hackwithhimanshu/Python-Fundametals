from pathlib import Path

paths = [Path("cats.txt"), Path("dogs.txt")]


for path in paths:
    try:
        print(f"\nContents of {path.name}")
        print(path.read_text())
    except FileNotFoundError:
        pass     