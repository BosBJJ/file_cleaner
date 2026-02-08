from cleaner import find_old_files
from pathlib import Path

if __name__ == "__main__":
    folder = Path("")
    days = 3

    old_files = find_old_files(folder=folder, days=days)
    for file in old_files:
        print(file)