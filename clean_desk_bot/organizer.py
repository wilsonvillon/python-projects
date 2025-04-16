# Imports
import os
import shutil


# Functions
def list_files(folder_path):
    return os.listdir(folder_path)

"""
Clean Desk Bot

This script scans a specified folder, detects file types by their extensions,
creates organized subfolders (e.g., 'PDF_FILES', 'JPG_FILES'), and moves the
corresponding files into their respective folders.

Useful for cleaning up download folders, project workspaces, or any cluttered
directory with mixed file types.

Modules used:
- os: For file and directory operations
- shutil: For moving files

Author: Wilson Villon
"""


def get_extension(filename):
    return os.path.splitext(filename)[1]


def move_file_to_subfolder(file_path, destination_folder):
    extension = get_extension(file_path)

    # Remove the dot from extension for folder naming
    ext_folder = extension[1:].upper() + "_FILES"
    destination_path = os.path.join(destination_folder, ext_folder)

    # Create the folder if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Build full source and destination file paths
    src = os.path.join(destination_folder, file_path)
    dest = os.path.join(destination_path, file_path)

    # Move the file
ls
shutil.move(src, dest)
    print(f"Moved {file_path} → {destination_path}")
    


# Executing / Testing
folder = "test_folder"
for file in list_files(folder):
    move_file_to_subfolder(file, folder)
