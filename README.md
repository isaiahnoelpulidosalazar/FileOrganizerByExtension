# File Organizer

A lightweight Python script that automatically sorts and organizes loose files into categorized folders based on their file extensions.

---

## Features

* **Extension-Based Sorting:** Moves files into subdirectories named after their extensions (e.g., `.pdf` files move to `pdf/`, `.png` files move to `png/`).
* **Conflict Resolution:** Safely renames files with `_1`, `_2` suffixes if a file with the same name already exists in the destination folder.
* **Scan Modes:** Supports both top-level directory cleanup and recursive subfolder scanning.
* **Audit Logging:** Automatically creates and appends execution logs to `organization_log.txt` in the target directory.
* **Zero Dependencies:** Built entirely using Python standard libraries (`pathlib`, `shutil`, `datetime`, `os`).

---

## Project Structure

```text
.
├── organizer.py           # Main script file
└── README.md              # Project documentation

```

---

## How It Works

1. **Scan Target Directory:** The script lists files in the specified path (either top-level only or recursively).
2. **Determine Extension Folder:** Identifies the file extension (or sets `no_extension` if missing).
3. **Handle Duplicates:** Checks if the target filename exists and appends an incremental numerical suffix if needed.
4. **Relocate File:** Moves the file into its respective extension folder using `shutil.move()`.
5. **Log Actions:** Records each file movement and a total count summary inside `organization_log.txt`.

---

## Installation & Requirements

* **Python 3.6+** (No external package installation required)

Clone or download the repository to your local system:

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer

```

---

## Configuration & Usage

Open `organize.py` (or your script file name) in a text editor and update the execution settings at the bottom:

```python
if __name__ == "__main__":
    # Specify the target directory to organize
    folder_to_organize = r"/path/to/your/folder"

    # Set to True to scan subdirectories, or False for top-level only
    SCAN_SUBFOLDERS = True

    organize_folder(folder_to_organize, include_subfolders=SCAN_SUBFOLDERS)

```

Run the script from your terminal:

```bash
python organizer.py

```

---

## Example Output

### Before Execution

```text
/Downloads
├── report.pdf
├── photo.png
└── document.pdf

```

### Terminal Output

```text
Moved: 'report.pdf' -> 'pdf/report.pdf'
Moved: 'photo.png' -> 'png/photo.png'
Moved: 'document.pdf' -> 'pdf/document.pdf'

Done! Organized 3 file(s). Summary saved to organization_log.txt

```

### After Execution

```text
/Downloads
├── organization_log.txt
├── pdf/
│   ├── report.pdf
│   └── document.pdf
└── png/
    └── photo.png

```

---

## Sample Log File Entry

Every execution appends details to `organization_log.txt`:

```text
--- Organization Run [Recursive (subfolders included)]: 2026-09-03 18:00:00 ---
Moved: 'document.pdf' -> 'pdf/document.pdf'
Moved: 'image.png' -> 'png/image.png'
Total files moved: 2

```

---

## License

Distributed under the MIT License. Feel free to modify and adapt for personal or commercial projects.