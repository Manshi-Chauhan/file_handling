This project is a Python-based program that reads data from a text file, finds specific words, replaces them with user-defined words, and saves the updated content back to the file.

The program also includes robust error handling to manage file-related issues such as missing files, permission errors, and invalid inputs.

🚀 Features
📖 Read data from a text file
🔍 Find specific words in the file
✏️ Replace words with user input
💾 Save updated content back to the file
⚠️ Handles errors gracefully:
File not found
Permission issues
Word not found
Unexpected errors
🛠️ Technologies Used
Python 3
File Handling
Exception Handling
String Manipulation
📂 How It Works
User enters the file name
User inputs:
Word to find
Word to replace
Program reads the file
Searches for the word
Replaces it with the new word
Saves the updated content back into the same file
▶️ Usage
Step 1: Run the program
python filename.py
Step 2: Provide input
Enter file name: data.txt  
Enter word to find: hello  
Enter word to replace with: hi  
📄 Example
Input File (data.txt)
hello world  
python is fun  
hello again  
Output File (after execution)
hi world  
python is fun  
hi again  
🛡️ Error Handling

The program handles the following errors:

❌ FileNotFoundError → when file does not exist
❌ PermissionError → when access is denied
⚠️ Word not found → informs user without crashing
❌ General Exception → handles unexpected errors
💡 Future Improvements
Case-insensitive replacement
Replace only whole words (not partial matches)
Create backup file before editing
Add GUI using Tkinter
Display number of replacements
👨‍💻 Author

Your Name
