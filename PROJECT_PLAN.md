# File Cleaner Web App – Plan

## Phase 1: Setup
- [X] Initialize Git repo
- [X] Create basic project structure
- [X] Add minimal web server (“Hello World”)

## Phase 2: Core Cleanup Logic
- [X] Write function to scan a folder for files
- [X] Compute file ages and filter by age threshold
- [X] Implement “dry run” listing of files to delete
- [X] Implement actual delete function

## Phase 3: Web UI
- [ ] HTML form for:
  - [ ] Folder path input
  - [ ] Age in days input
- [ ] Route to handle form submit and run scan
- [ ] Page to display candidate files (name, path, date)
- [ ] Add checkboxes for file selection
- [ ] “Delete selected” action and confirmation page

## Phase 4: Safety & Polish
- [ ] Add confirmation step before delete
- [ ] Handle invalid folder / errors gracefully
- [ ] Optional “move to Trash folder” instead of permanent delete
- [ ] Basic CSS to make UI readable

## Phase 5: Make It Shareable
- [ ] Create `README.md` (what it does, how to run it)
- [ ] Add screenshots of the app
- [ ] Add dependency file (`requirements.txt` or similar)