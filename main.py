from student import Student
from course import Course
from professor import Professor
from login_user import LoginUser


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
        print("8. Average Marks by Course")
        print("9. Median Marks by Course")
        print("10. Generate Course Report")
        print("11. Add Course")
        print("12. Display All Courses")
        print("13. Delete Course")
        print("14. Update Course")
        print("15. Add Professor")
        print("16. Display All Professors")
        print("17. Delete Professor")
        print("18. Update Professor")
        print("19. Add Login User")
        print("20. Display All Login Users")
        print("21. Login")
        print("22. Exit")

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
            course_id = input("Enter course ID: ")
            Student.calculate_average_marks_by_course(course_id)

        elif choice == "9":
            course_id = input("Enter course ID: ")
            Student.calculate_median_marks_by_course(course_id)

        elif choice == "10":
            course_id = input("Enter course ID: ")
            Student.generate_course_report(course_id)

        elif choice == "11":
            Course.add_new_course()

        elif choice == "12":
            Course.display_all_courses()

        elif choice == "13":
            course_id = input("Enter the course ID to delete: ")
            Course.delete_course(course_id)

        elif choice == "14":
            course_id = input("Enter the course ID to update: ")
            Course.update_course(course_id)

        elif choice == "15":
            Professor.add_new_professor()

        elif choice == "16":
            Professor.display_all_professors()

        elif choice == "17":
            professor_id = input("Enter the professor ID to delete: ")
            Professor.delete_professor(professor_id)

        elif choice == "18":
            professor_id = input("Enter the professor ID to update: ")
            Professor.update_professor(professor_id)

        elif choice == "19":
            LoginUser.add_new_login_user()

        elif choice == "20":
            LoginUser.display_all_login_users()

        elif choice == "21":
            LoginUser.login()

        elif choice == "22":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()