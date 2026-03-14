from student import Student


def main():
    while True:
        print("\nCheckMyGrade - Student Menu")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Student.add_new_student()

        elif choice == "2":
            Student.display_all_students()

        elif choice == "3":
            email = input("Enter the email of the student to delete: ")
            Student.delete_student(email)

        elif choice == "4":
            email = input("Enter the email of the student to update: ")
            Student.update_student_record(email)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()