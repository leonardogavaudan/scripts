import os
from typing import Dict, Set


def group_files_by_extension(directory: str) -> Dict[str, Set[str]]:
    files_by_extension = {}

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            ext = os.path.splitext(file)[1]
            if ext not in files_by_extension:
                files_by_extension[ext] = set()
            files_by_extension[ext].add(file)

    return files_by_extension


def main():
    dir_path = os.path.expanduser("~/Downloads/iCloud Photos/")
    extension_to_files = group_files_by_extension(dir_path)
    files_to_delete = []

    for file in extension_to_files[".MOV"]:
        file_root = file.split(".")[0]
        heic_file = file_root + ".HEIC"
        if heic_file in extension_to_files[".HEIC"]:
            files_to_delete.append(file)

    print(f"You are about to delete {len(files_to_delete)} files:")
    for file in files_to_delete:
        print(file)

    confirm = input("Do you want to proceed? (y/n): ").lower()

    if confirm == "y":
        for file in files_to_delete:
            os.remove(os.path.join(dir_path, file))
        print("Files deleted.")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
