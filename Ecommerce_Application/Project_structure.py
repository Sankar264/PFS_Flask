from pathlib import Path

PROJECT_NAME = ""
folders = [
    "templates",
    "static",
    "database"
]
files = [
    "README.md",
    ".gitignore",
    "requirements.txt",
    "app.py",
    "database/__init__.py",
    "utils.py",
    ".env"
]
#create project structure
root = Path(PROJECT_NAME)
root.mkdir(exist_ok=True)
print(root)
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)
#create files
for file in files:
    path = root / file
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.touch()
print(f"Project structure for '{PROJECT_NAME}' created successfully.")
