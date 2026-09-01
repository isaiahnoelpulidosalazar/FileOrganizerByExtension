from datetime import datetime
import os
import shutil
from pathlib import Path


def organize_folder(target_directory, include_subfolders=False):
    target_path = Path(target_directory)

    if not target_path.exists() or not target_path.is_dir():
        print(f"Error: Path '{target_directory}' is not a valid directory.")
        return

    log_file_path = target_path / "organization_log.txt"
    moved_count = 0

    if include_subfolders:
        items = [p for p in target_path.rglob("*") if p.is_file()]
    else:
        items = [p for p in target_path.iterdir() if p.is_file()]

    with open(log_file_path, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scan_mode = "Recursive (subfolders included)" if include_subfolders else "Top-level only"
        log_file.write(f"--- Organization Run [{scan_mode}]: {timestamp} ---\n")

        for item in items:
            if item.resolve() == log_file_path.resolve():
                continue

            ext = item.suffix[1:].lower() if item.suffix else "no_extension"
            dest_folder = target_path / ext

            if item.parent.resolve() == dest_folder.resolve():
                continue

            dest_folder.mkdir(exist_ok=True)

            dest_file_path = dest_folder / item.name

            counter = 1
            original_stem = item.stem
            while dest_file_path.exists():
                dest_file_path = dest_folder / f"{original_stem}_{counter}{item.suffix}"
                counter += 1

            try:
                rel_source = item.relative_to(target_path)
            except ValueError:
                rel_source = item.name

            shutil.move(str(item), str(dest_file_path))

            log_entry = f"Moved: '{rel_source}' -> '{ext}/{dest_file_path.name}'\n"
            log_file.write(log_entry)
            print(log_entry.strip())

            moved_count += 1

        log_file.write(f"Total files moved: {moved_count}\n")

    print(f"\nDone! Organized {moved_count} file(s). Summary saved to organization_log.txt")


if __name__ == "__main__":
    # Replace with the path to the folder you want to clean up
    # Example for Windows: r"C:\Users\YourName\Downloads"
    # Example for Mac/Linux: "/Users/YourName/Downloads"
    folder_to_organize = r"/folder"

    SCAN_SUBFOLDERS = True

    organize_folder(folder_to_organize, include_subfolders=SCAN_SUBFOLDERS)