from student import Student
from course import Course
from professor import Professor


def main():
    while True:
        print("\nCheckMyGrade - Main Menu")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student by Email")
        print("6. Sort Students by Marks")
        print("7. Sort Students by First Name")
        print("8. Add Course")
        print("9. Display All Courses")
        print("10. Delete Course")
        print("11. Update Course")
        print("12. Add Professor")
        print("13. Display All Professors")
        print("14. Delete Professor")
        print("15. Update Professor")
        print("16. Exit")

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
            email = input("Enter the email of the student to search: ")
            Student.search_student_by_email(email)

        elif choice == "6":
            Student.sort_students_by_marks()

        elif choice == "7":
            Student.sort_students_by_first_name()

        elif choice == "8":
            Course.add_new_course()

        elif choice == "9":
            Course.display_all_courses()

        elif choice == "10":
            course_id = input("Enter the course ID to delete: ")
            Course.delete_course(course_id)

        elif choice == "11":
            course_id = input("Enter the course ID to update: ")
            Course.update_course(course_id)

        elif choice == "12":
            Professor.add_new_professor()

        elif choice == "13":
            Professor.display_all_professors()

        elif choice == "14":
            professor_id = input("Enter the professor ID to delete: ")
            Professor.delete_professor(professor_id)

        elif choice == "15":
            professor_id = input("Enter the professor ID to update: ")
            Professor.update_professor(professor_id)

        elif choice == "16":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()