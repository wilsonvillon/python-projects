# Clean Desk Bot v3 🧠📂

**Clean Desk Bot v3** is a Python automation script that organizes files into categorized subfolders based on extension types. Unlike previous versions, this version reads sorting rules from a configuration file (`rules.json`), making it flexible and easy to customize without changing the code.

---

## 🚀 Features

- Dynamically loads sorting rules from JSON
- Detects file types using extensions
- Automatically creates destination folders
- Moves files into categorized subdirectories
- Easy to update categories via configuration

---

## 🧠 Skills Demonstrated

- File I/O and JSON parsing
- Modular, reusable function design
- Real-world automation principles
- Data normalization and conditionals
- Decoupling logic from source code

---

## 🧪 Example Configuration (`rules.json`)

```json
{
  "Documents": ["pdf", "docx", "txt"],
  "Images": ["jpg", "png", "gif"],
  "Installers": ["exe", "msi"],
  "Design": ["psd", "ai", "fig"]
}
🧪 Example Output
lua
Copy
Edit
Moved resume.pdf → Documents/
Moved logo.png → Images/
Moved app_installer.exe → Installers/
Moved design_mockup.psd → Design/
Moved unknown_file.zip → Other/
🔧 How to Use
Clone or download the project

Place mixed files into the test_folder/

Edit the rules.json file to suit your needs

Run the script:

bash
Copy
Edit
python clean_desk_bot_v3.py
🙋‍♂️ Author
Created by Wilson Villon
Python automation builder | Problem solver | Learning with purpose

