def show_menu():
    """
    Displays menu options.
    """
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Register Students")
    print("2. List Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def read_positive_int(message):
    """
    Validates positive integer input.
    """
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Must be an integer.")


def read_text(message):
    """
    Validates text input.

    - Not empty
    - Not only numbers
    - Only letters, numbers and spaces
    """
    while True:
        text = input(message).strip()

        if not text:
            print("Field cannot be empty.")
            continue

        if text.isdigit():
            print("Cannot contain only numbers.")
            continue

        valid = True
        for c in text:
            if not (c.isalpha() or c.isdigit() or c.isspace()):
                valid = False
                break

        if not valid:
            print("Invalid format. Only letters, numbers and spaces.")
            continue

        return text


def read_only_text(message):
    """
    Validates text input.

    - Not empty
    - Not only numbers
    - Only letters and spaces
    """
    while True:
        text = input(message).strip()

        if not text:
            print("Field cannot be empty.")
            continue

        if text.isdigit():
            print("Cannot contain only numbers.")
            continue

        valid = True
        for c in text:
            if not (c.isalpha() or c.isspace()):
                valid = False
                break

        if not valid:
            print("Invalid format. Only letters and spaces.")
            continue

        return text


def get_student_data():
    """
    Collects student data.
    """
    return {
        "id": read_positive_int("Student ID: "),
        "name": read_only_text("Name: "),
        "age": read_positive_int("Age: "),
        "program": read_text("Program: "),
        # "status": "active",
        "status": read_only_text("Status(Active/Inactive): ")
    }


def get_update_data():
    """
    Collects student data strictly for update.
    """
    return {
        "name": read_only_text("Name: "),
        "age": read_positive_int("Age: "),
        "program": read_text("Program: "),
        "status": read_only_text("Status(Active/Inactive): ")
    }
