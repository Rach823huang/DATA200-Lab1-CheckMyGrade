import unittest
import os
import time
import io
from contextlib import redirect_stdout
from unittest.mock import patch

from student import Student
from course import Course
from professor import Professor
from file_manager import write_csv_file, read_csv_file, append_csv_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STUDENT_FILE = os.path.join(BASE_DIR, "student.csv")
COURSE_FILE = os.path.join(BASE_DIR, "course.csv")
PROFESSOR_FILE = os.path.join(BASE_DIR, "professor.csv")


class TestCheckMyGrade(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Backup original file contents
        cls.student_backup = cls._read_raw_file(STUDENT_FILE)
        cls.course_backup = cls._read_raw_file(COURSE_FILE)
        cls.professor_backup = cls._read_raw_file(PROFESSOR_FILE)

    @classmethod
    def tearDownClass(cls):
        # Restore original files after all tests finish
        cls._write_raw_file(STUDENT_FILE, cls.student_backup)
        cls._write_raw_file(COURSE_FILE, cls.course_backup)
        cls._write_raw_file(PROFESSOR_FILE, cls.professor_backup)

    @classmethod
    def _read_raw_file(cls, path):
        if os.path.exists(path):
            with open(path, "r", newline="") as f:
                return f.read()
        return ""

    @classmethod
    def _write_raw_file(cls, path, content):
        with open(path, "w", newline="") as f:
            f.write(content)

    def setUp(self):
        # Reset files before each test
        write_csv_file(
            "student.csv",
            ["email_address", "first_name", "last_name", "course_id", "grade", "marks"],
            []
        )
        write_csv_file(
            "course.csv",
            ["course_id", "course_name", "description"],
            []
        )
        write_csv_file(
            "professor.csv",
            ["professor_id", "name", "email_address", "rank", "course_id"],
            []
        )

    # ----------------------
    # STUDENT TESTS
    # ----------------------
    @patch("builtins.input", side_effect=[
        "alice@gmail.com", "Alice", "Wong", "DATA200", "A", "95"
    ])
    def test_add_student(self, mock_inputs):
        Student.add_new_student()
        students = read_csv_file("student.csv")
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][0], "alice@gmail.com")
        self.assertEqual(students[0][1], "Alice")

    def test_delete_student(self):
        append_csv_file("student.csv", ["alice@gmail.com", "Alice", "Wong", "DATA200", "A", "95"])
        append_csv_file("student.csv", ["bob@gmail.com", "Bob", "Lee", "DATA200", "B", "85"])

        Student.delete_student("alice@gmail.com")
        students = read_csv_file("student.csv")

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][0], "bob@gmail.com")

    @patch("builtins.input", side_effect=[
        "newalice@gmail.com", "Alicia", "Wong", "DATA201", "A", "97"
    ])
    def test_update_student(self, mock_inputs):
        append_csv_file("student.csv", ["alice@gmail.com", "Alice", "Wong", "DATA200", "A", "95"])

        Student.update_student_record("alice@gmail.com")
        students = read_csv_file("student.csv")

        self.assertEqual(students[0][0], "newalice@gmail.com")
        self.assertEqual(students[0][1], "Alicia")
        self.assertEqual(students[0][3], "DATA201")
        self.assertEqual(students[0][5], "97")

    def test_load_1000_students_and_search_timing(self):
        # create 1000 student records
        for i in range(1000):
            append_csv_file(
                "student.csv",
                [f"user{i}@gmail.com", f"First{i}", f"Last{i}", "DATA200", "A", str(80 + (i % 20))]
            )

        output = io.StringIO()
        start_time = time.time()
        with redirect_stdout(output):
            Student.search_student_by_email("user999@gmail.com")
        end_time = time.time()

        result = output.getvalue()
        self.assertIn("user999@gmail.com", result)
        self.assertIn("Search time:", result)

        total_time = end_time - start_time
        print(f"\nTotal time for search test with 1000 records: {total_time:.8f} seconds")

    def test_sort_students_by_marks_and_email_timing(self):
        # create 1000 student records
        for i in range(1000):
            append_csv_file(
                "student.csv",
                [f"user{999-i}@gmail.com", f"First{i}", f"Last{i}", "DATA200", "A", str(60 + (i % 40))]
            )

        # sort by marks ascending
        output1 = io.StringIO()
        start1 = time.time()
        with redirect_stdout(output1):
            Student.sort_students_by_marks()
        end1 = time.time()

        # sort by marks descending
        output2 = io.StringIO()
        start2 = time.time()
        with redirect_stdout(output2):
            Student.sort_students_by_marks_descending()
        end2 = time.time()

        # sort by email
        output3 = io.StringIO()
        start3 = time.time()
        with redirect_stdout(output3):
            Student.sort_students_by_email()
        end3 = time.time()

        self.assertIn("Students Sorted by Marks", output1.getvalue())
        self.assertIn("Descending", output2.getvalue())
        self.assertIn("Students Sorted by Email", output3.getvalue())

        print(f"\nSort by marks ascending time: {end1 - start1:.8f} seconds")
        print(f"Sort by marks descending time: {end2 - start2:.8f} seconds")
        print(f"Sort by email time: {end3 - start3:.8f} seconds")

    # ----------------------
    # COURSE TESTS
    # ----------------------
    @patch("builtins.input", side_effect=[
        "DATA201", "Database Systems", "Intro to SQL"
    ])
    def test_add_course(self, mock_inputs):
        Course.add_new_course()
        courses = read_csv_file("course.csv")
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0][0], "DATA201")

    def test_delete_course(self):
        append_csv_file("course.csv", ["DATA201", "Database Systems", "Intro to SQL"])
        append_csv_file("course.csv", ["DATA202", "Python", "Advanced Python"])

        Course.delete_course("DATA201")
        courses = read_csv_file("course.csv")

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0][0], "DATA202")

    @patch("builtins.input", side_effect=[
        "DATA203", "Data Mining", "Mining concepts"
    ])
    def test_update_course(self, mock_inputs):
        append_csv_file("course.csv", ["DATA201", "Database Systems", "Intro to SQL"])

        Course.update_course("DATA201")
        courses = read_csv_file("course.csv")

        self.assertEqual(courses[0][0], "DATA203")
        self.assertEqual(courses[0][1], "Data Mining")

    # ----------------------
    # PROFESSOR TESTS
    # ----------------------
    @patch("builtins.input", side_effect=[
        "P100", "Dr. Smith", "smith@gmail.com", "Professor", "DATA201"
    ])
    def test_add_professor(self, mock_inputs):
        Professor.add_new_professor()
        professors = read_csv_file("professor.csv")
        self.assertEqual(len(professors), 1)
        self.assertEqual(professors[0][0], "P100")

    def test_delete_professor(self):
        append_csv_file("professor.csv", ["P100", "Dr. Smith", "smith@gmail.com", "Professor", "DATA201"])
        append_csv_file("professor.csv", ["P200", "Dr. Lee", "lee@gmail.com", "Associate", "DATA202"])

        Professor.delete_professor("P100")
        professors = read_csv_file("professor.csv")

        self.assertEqual(len(professors), 1)
        self.assertEqual(professors[0][0], "P200")

    @patch("builtins.input", side_effect=[
        "P300", "Dr. Brown", "brown@gmail.com", "Assistant", "DATA203"
    ])
    def test_update_professor(self, mock_inputs):
        append_csv_file("professor.csv", ["P100", "Dr. Smith", "smith@gmail.com", "Professor", "DATA201"])

        Professor.update_professor("P100")
        professors = read_csv_file("professor.csv")

        self.assertEqual(professors[0][0], "P300")
        self.assertEqual(professors[0][1], "Dr. Brown")
        self.assertEqual(professors[0][4], "DATA203")


if __name__ == "__main__":
    unittest.main()