# Clean Desk Bot v2 🧹📂

**Clean Desk Bot v2** is an upgraded Python automation tool that organizes files based on their category (Images, Documents, Installers, etc.) rather than just file extensions. It scans a specified folder, detects file types, and moves them into neatly categorized subfolders.

---

## 🚀 Features

- Detects file extensions and maps them to smart categories
- Creates folders like `Documents/`, `Images/`, `Installers/`, `Photoshop/`, and `Other/`
- Automatically moves files into their appropriate subfolder
- Simple, fast, and cross-platform

---

## 🧠 Skills Demonstrated

- Advanced dictionary usage for data mapping
- File system operations with `os` and `shutil`
- Clean, reusable function structure
- Real-world automation and problem solving

---

## 🧪 Example

**Before:**
test_folder/ ├── photo.jpg ├── resume.pdf ├── installer.exe ├── design.psd ├── unknownfile.ai

**After:**
test_folder/ ├── Images/photo.jpg ├── Documents/resume.pdf ├── Installers/installer.exe ├── Photoshop/design.psd ├── Other/unknownfile.ai

---

## 🔧 How to Use

1. Place mixed files into the `test_folder/`
2. Run the script:

```bash
python organizer.py
Check your folder to see everything automatically sorted into subfolders

🙋‍♂️ Author
Created by Wilson Villon
Python automation enthusiast, problem solver, and real-world tool builder.
