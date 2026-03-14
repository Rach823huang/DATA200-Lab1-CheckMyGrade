from file_manager import read_csv_file, append_csv_file, write_csv_file
import time
import statistics

class Student:
    def __init__(self, email_address, first_name, last_name, course_id, grade, marks):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def to_list(self):
        return [
            self.email_address,
            self.first_name,
            self.last_name,
            self.course_id,
            self.grade,
            self.marks
        ]

    def display_record(self):
        print(
            f"Email: {self.email_address}, "
            f"Name: {self.first_name} {self.last_name}, "
            f"Course ID: {self.course_id}, "
            f"Grade: {self.grade}, "
            f"Marks: {self.marks}"
        )

    @staticmethod
    def add_new_student():
        email_address = input("Enter email address: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        course_id = input("Enter course ID: ")
        grade = input("Enter grade: ")
        marks = input("Enter marks: ")

        student = Student(email_address, first_name, last_name, course_id, grade, marks)
        append_csv_file("student.csv", student.to_list())
        print("Student added successfully.")

    @staticmethod
    def display_all_students():
        students = read_csv_file("student.csv")
        if not students:
            print("No student records found.")
            return

        print("\nStudent Records:")
        for row in students:
            print(row)

    @staticmethod
    def delete_student(email_to_delete):
        students = read_csv_file("student.csv")
        updated_students = []

        found = False
        for row in students:
            if row[0] != email_to_delete:
                updated_students.append(row)
            else:
                found = True

        if found:
            header = ["email_address", "first_name", "last_name", "course_id", "grade", "marks"]
            write_csv_file("student.csv", header, updated_students)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    @staticmethod
    def update_student_record(email_to_update):
        students = read_csv_file("student.csv")
        updated_students = []
        found = False

        for row in students:
            if row[0] == email_to_update:
                found = True
                print("Enter new values for the student:")
                new_email = input("Enter new email address: ")
                new_first_name = input("Enter new first name: ")
                new_last_name = input("Enter new last name: ")
                new_course_id = input("Enter new course ID: ")
                new_grade = input("Enter new grade: ")
                new_marks = input("Enter new marks: ")

                updated_students.append([
                    new_email,
                    new_first_name,
                    new_last_name,
                    new_course_id,
                    new_grade,
                    new_marks
                ])
            else:
                updated_students.append(row)

        if found:
            header = ["email_address", "first_name", "last_name", "course_id", "grade", "marks"]
            write_csv_file("student.csv", header, updated_students)
            print("Student updated successfully.")
        else:
            print("Student not found.")

    @staticmethod
    def search_student_by_email(email_to_search):
        students = read_csv_file("student.csv")

        start_time = time.time()

        found = False
        for row in students:
            if row[0] == email_to_search:
                found = True
                print("\nStudent Found:")
                print(row)
                break

        end_time = time.time()
        elapsed_time = end_time - start_time

        if not found:
            print("Student not found.")

        print(f"Search time: {elapsed_time:.8f} seconds")

    @staticmethod
    def sort_students_by_marks():
        students = read_csv_file("student.csv")

        if not students:
            print("No student records found.")
            return

        sorted_students = sorted(students, key=lambda row: float(row[5]))

        print("\nStudents Sorted by Marks (Ascending):")
        for row in sorted_students:
            print(row)

    @staticmethod
    def sort_students_by_first_name():
        students = read_csv_file("student.csv")

        if not students:
            print("No student records found.")
            return

        sorted_students = sorted(students, key=lambda row: row[1].lower())

        print("\nStudents Sorted by First Name (A-Z):")
        for row in sorted_students:
            print(row)

    @staticmethod
    def calculate_average_marks_by_course(course_id):
        students = read_csv_file("student.csv")

        marks_list = []
        for row in students:
            if row[3] == course_id:
                marks_list.append(float(row[5]))

        if not marks_list:
            print("No student records found for this course.")
            return

        average_marks = sum(marks_list) / len(marks_list)
        print(f"Average marks for course {course_id}: {average_marks:.2f}")

    @staticmethod
    def calculate_median_marks_by_course(course_id):
        students = read_csv_file("student.csv")

        marks_list = []
        for row in students:
            if row[3] == course_id:
                marks_list.append(float(row[5]))

        if not marks_list:
            print("No student records found for this course.")
            return

        median_marks = statistics.median(marks_list)
        print(f"Median marks for course {course_id}: {median_marks:.2f}")

    @staticmethod
    def generate_course_report(course_id):
        students = read_csv_file("student.csv")

        course_students = []
        for row in students:
            if row[3] == course_id:
                course_students.append(row)

        if not course_students:
            print("No student records found for this course.")
            return

        print(f"\nCourse Report for {course_id}:")
        for row in course_students:
            print(row)