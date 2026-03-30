# 🎓 Student Registration System
---

## 🚀 Features

- Register new students. 
- Display all registered students.
- Search students by ID.  
- Update student information.  
- Delete students by ID 
- Save data to a CSV file  
---
## 🧱 Project Structure

The project is organized into the following modules:

### 📄 `main.py`
Entry point of the application.  
It initializes the system, loads existing data from the CSV file, and controls the main program loop.

It also containg all reusable `def` functions for input validation to ensure data integrity, such as:

- Positive integer validation  
- Non-empty text validation  
- Invalid input format validation 
- Not only numbers 
---

### ⚙️ `crud.py`
Contains the core student registratin logic of the system, including:

- Student registration  
- Displaying the student list  
- Searching for a student by ID  
- Updating student data  
- Deleting students 

---
## 💾 Data Storage

### 💾 `student.csv`
The system stores the data in a CSV file for data persistance.

`data/students.csv`
With the following format.
### Data Format (CSV)

| id | name      | age | program | status |
|----|----------|-----|-----------|--------|
| 1  | Juan Perez | 25  | Systems Engineering | Active |


Each record contains:

- `Id`: Unique identifier
- `Name`: Student name
- `Age`: Student age
- `Program`: Student Program
- `Status`: (Active/Inactive)

---
