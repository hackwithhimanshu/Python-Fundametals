from pathlib import Path

path = Path("10/Do it yourself/learning_python.txt")


content = path.read_text()
print(content.replace('python', 'C'))

