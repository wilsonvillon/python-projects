"""
Clean Desk Bot v3

This version of Clean Desk Bot dynamically organizes files by category based on
rules loaded from a JSON configuration file. It scans a specified folder,
detects each file's extension, and moves the file into a categorized subfolder.

This version decouples logic from code, allowing easy updates by editing rules.json.

Author: Wilson Villon
"""

# Imports
import os, json, shutil

with open("rules.json", "r") as file:
    rules = json.load(file)

# Returns a list of all items in the folder (files and folders)
def list_files(folder_path):
    return os.listdir(folder_path)

def get_extension(filename):
    return os.path.splitext(filename)[1]

def get_category_from_rules(rules, extension):
    for category, extensions in rules.items():
        if extension in extensions:
            return category
    return "Other"


def move_file_to_category(file_name, folder_path, rules):
    # Get file extension (without the dot)
    extension = get_extension(file_name).lstrip('.').lower()

    # Find the matching category from the rules
    category = get_category_from_rules(rules, extension)

    # Build the destination folder path
    destination_path = os.path.join(folder_path, category)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Build source and destination file paths
    src = os.path.join(folder_path, file_name)
    dest = os.path.join(destination_path, file_name)

    # Move the file
    shutil.move(src, dest)
    print(f"Moved {file_name} → {destination_path}")


folder = "test_folder"
for file in list_files(folder):
    if os.path.isfile(os.path.join(folder, file)):  # skip subfolders
        move_file_to_category(file, folder, rules)
