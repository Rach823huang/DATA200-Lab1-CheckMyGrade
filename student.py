import csv


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