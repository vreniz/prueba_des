# 🎓 Student Registration System
---

## 🚀 Features

- Register new students. 
- Display all registered students.
- Search students by ID.  
- Update student information by ID.  
- Delete students by ID. 
- Save data to a CSV file.  
---
## 🧱 Project Structure

The project is organized into the following modules:

### 📄 `main.py`
Entry point of the application.  
It initializes the system, loads existing data from the CSV file, and controls the main program loop.

### ✅ `validate.py`
It  contains all reusable `def` functions for input validation to ensure data integrity, such as:

- Positive integer validation. 
- Non-empty text validation. 
- Invalid input format validation. 
- Not only numbers. 


### ⚙️ `crud.py`
Contains the core student registratin logic of the system, including:

- Student registration.  
- Displaying the student list.  
- Searching for a student by ID.  
- Updating student data. 
- Deleting students.

---
## 💾 Data Storage

### 💾 `student.csv`
The system stores the data in a CSV file for data persistance, in the file path:

`data/students.csv`

With the following format.
### Data Format (CSV)

| id | name      | age | program | status |
|----|----------|-----|-----------|--------|
| 1  | Juan Perez | 25  | Systems Engineering | Active |


Each record contains:

- `Id`: Unique identifier.
- `Name`: Student name.
- `Age`: Student age.
- `Program`: Student Program.
- `Status`: (Active/Inactive).

---
## 🛠 Technologies Used

- Python 🐍 
- CSV file handling (`csv` module)  
- Lists and dictionaries.
- Modular programming. 
- Input validation. 
- Exception handling.

---

## ▶️ How to Run

For running this project use the terminal with the following command.

```bash
python3 main.py
```
This would display the program *MENU* in the console as it follows:
### *📋 Menu Options:*
```
--- STUDENT MANAGEMENT SYSTEM ---
1. Register Students
2. List Students
3. Search Student by ID
4. Update Student
5. Delete Student
6. Exit
Choose an option: 1
```
With this, the user is able to pick any of the previous options to execute the *Student Registration Program*.
### 🧠 Input Validation

The system ensures valid user input through reusable validation functions:

- Prevents empty values.
- Ensures numeric inputs are positive and not 0.
- Avoids invalid data formats.

This guarantees:

- Data consistency.
- Better user experience.
- Reduced runtime errors.
---
## Author
*Vanessa Fontalvo Reniz* | Systems Engineer | Aspiring Software Developer.