from crud import *
from validate import *


if __name__ == "__main__":
    """
    While true infinitive loop for menu options control.
    """
    while True:

        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            data = get_student_data()
            if create_student(data):
                print("Student registered successfully.")

        elif option == "2":
            students = read_students()
            if students:
                print("\nSTUDENTS:")
                for s in students:
                    print(s)
            else:
                print("No students found.")

        elif option == "3":
            try:
                student_id = int(input("Enter Student ID: "))
                result = find_student_by_id(student_id)
                print(result if result else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "4":
            try:
                student_id = int(input("Enter Student ID to update: "))
                updated = update_student(student_id, get_update_data())
                print("Updated." if updated else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "5":
            try:
                student_id = int(input("Enter Student ID to delete: "))
                print("Deleted." if delete_student(
                    student_id) else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
