from pathlib import Path
from datetime import datetime, timedelta
import sys

def find_old_files(folder: Path, days: int):
    folder_path = Path(folder).resolve()
    #Silly app deleted itself so now I have to make sure it doesn't
    project_root = Path(__file__).parent.resolve()
    if folder_path == project_root or project_root in folder_path.parents:
        raise Exception("Refusing to clean inside the project directory.")
    
    to_be_deleted = []

    if not folder_path.is_dir():
        raise Exception("Incorrect Path, please check your spelling")
    
    time_now = datetime.now()
    
    for path in folder_path.iterdir():
        if path.is_dir():
            to_be_deleted.extend(find_old_files(path, days))
        if path.is_file():
            if path.suffix == ".ini":
                continue
            mtime = path.stat().st_mtime
            modified_time = datetime.fromtimestamp(mtime)
            cutoff = time_now - timedelta(days=days)
            if modified_time < cutoff:
                to_be_deleted.append(path)

    return to_be_deleted

def delete_files(files: list[Path]):
    for path in files:
        if path.is_file():
            try:
                path.unlink()
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Error: could not delete {path}: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 cleaner.py /path/to/folder DAYS [--dry-run]")
        return
    folder = Path(sys.argv[1])
    days = int(sys.argv[2])
    dry_run = "--dry-run" in sys.argv
    

    old_files = find_old_files(folder, days)

    if not old_files:
        print("No files to delete")
        return
    
    print(f"These files are older than {days} days:")
    for file in old_files:
        print(f"  {file}")

    if dry_run:
        print("\nNo files were deleted")
        return
    
    response = input("Proceed with deletion? [y/n]").strip().lower()

    if response == "y":
        delete_files(old_files)
        print("Deletion process has been completed")

    else:
        print("Aborted. No files were deleted")

if __name__ == "__main__":
    main()