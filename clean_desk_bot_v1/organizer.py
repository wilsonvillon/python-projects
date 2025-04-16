"""
Clean Desk Bot v1

This script organizes files in a specified folder by detecting file extensions
and creating subfolders named after those extensions (e.g., 'PDF_FILES', 'JPG_FILES').

Each file is moved into its corresponding extension-based folder. Useful for 
basic organization of mixed file types in a single directory.

Usage:
- Place your files into the "test_folder" or any target folder
- Run the script to organize files by file type

Author: Wilson Villon
"""


# Imports
import os
import shutil


# Returns a list of all items in the folder (files and folders)
def list_files(folder_path):
    return os.listdir(folder_path)


# Extracts the file extension from a given filename (e.g., '.jpg')
def get_extension(filename):
    return os.path.splitext(filename)[1]


# Moves a file into a subfolder named after its extension
def move_file_to_subfolder(file_path, destination_folder):
    extension = get_extension(file_path)

    # Format subfolder name: remove dot and add suffix (e.g., 'PDF_FILES')
    ext_folder = extension[1:].upper() + "_FILES"
    destination_path = os.path.join(destination_folder, ext_folder)

    # Create the folder if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Build full source and destination file paths
    src = os.path.join(destination_folder, file_path)
    dest = os.path.join(destination_path, file_path)

    # Move the file
    shutil.move(src, dest)
    print(f"Moved {file_path} → {destination_path}")
    

# Run the bot on the target folder
folder = "test_folder"
for file in list_files(folder):
    move_file_to_subfolder(file, folder)
