"""
Clean Desk Bot v2

This script organizes files in a specified folder by detecting their file types
(extensions), mapping them to categories (e.g., Images, Documents, Installers), 
and moving them into neatly categorized subfolders.

Usage:
- Place your files into the "test_folder" or any target folder
- Run the script to organize files by category

Author: Wilson Villon
"""


# Imports
import os, shutil


# Returns a list of all items in the folder (files and folders)
def list_files(folder_path):
    return os.listdir(folder_path)


# Extracts the file extension from a given filename (e.g., '.jpg')
def get_extension(filename):
    return os.path.splitext(filename)[1]


# Maps file extensions to their corresponding folder category
def get_category(extension):
    ext_category = {
        "jpg": "Images",
        "png": "Images",
        "pdf": "Documents",
        "exe": "Installers",
        "psd": "Photoshop",
        "txt": "Documents",
        }

    # Normalize extension: remove leading dot and convert to lowercase
    key = extension.lstrip('.').lower()

    # Return category or 'Other' if extension is unrecognized
    return ext_category.get(key, "Other")


# Moves a file to its category-based subfolder
def move_file_to_subfolder(file_path, destination_folder):
    extension = get_extension(file_path)
    category = get_category(extension)

    destination_path = os.path.join(destination_folder, category)

    # Create the category folder if it doesn't already exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Build full paths for source and destination
    src = os.path.join(destination_folder, file_path)
    dest = os.path.join(destination_path, file_path)

    # Move the file
    shutil.move(src, dest)
    print(f"Moved {file_path} → {destination_path}") 

    
# Run the bot on the target folder
folder = "test_folder"
for file in list_files(folder):
    move_file_to_subfolder(file, folder)
