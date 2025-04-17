# Clean Desk Bot v1🧹📂

**Clean Desk Bot** is a Python automation script that organizes files in a folder by file type. It scans a target directory, detects file extensions, creates subfolders (like `PDF_FILES/`, `JPG_FILES/`, etc.), and moves each file into its appropriate folder.

---

## 🚀 Features

- Automatically detects file types using extensions
- Creates folders dynamically based on extension
- Moves files into neatly organized subdirectories
- Works cross-platform (Windows/macOS)

---

## 🧠 Skills Demonstrated

- File system operations with `os` and `shutil`
- String manipulation and path handling
- Writing reusable automation logic
- Building a fully testable, real-world tool

---

## 🧪 Example

**Before:**

test_folder/ ├── resume.pdf ├── photo.jpg ├── document.txt

**After:**

test_folder/ ├── PDF_FILES/resume.pdf ├── JPG_FILES/photo.jpg ├── TXT_FILES/document.txt

---

## 🔧 How to Use

1. Drop your mixed files into the `test_folder` (or any folder of your choice)
2. Update the folder name in `organizer.py`
3. Run the script:
   python organizer.py

```bash
🙋‍♂️ Author
Created by Wilson Villon
Python problem solver in training — focused on automation, AI, and web development.
