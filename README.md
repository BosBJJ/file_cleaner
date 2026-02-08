# File Cleaner Web App

This app is used to find files older than your input number of days and optionally delete them. 

## Usage
```bash
python3 cleaner.py /path/to/folder DAYS [--dry-run]
```

## Notes (WSL)

If you run this in WSL, Windows paths like `C:\Users\...` are available under `/mnt/c/...`.
