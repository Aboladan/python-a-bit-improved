from pathlib import Path

path = Path("Ajike")
print(path.exists())

path = Path()
for file in path.glob('*.py'):
    print(file)