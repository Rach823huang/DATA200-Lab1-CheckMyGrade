from student import Student
from file_manager import append_csv_file, read_csv_file


def main():
    print("CheckMyGrade - Lab 1")

    # create one sample student
    student1 = Student(
        "rachel@gmail.com",
        "Rachel",
        "Huang",
        "DATA200",
        "A",
        "95"
    )

    # save to csv
    append_csv_file("student.csv", student1.to_list())

    print("Student added successfully.\n")

    # display all student rows from csv
    students = read_csv_file("student.csv")
    print("Current student.csv data:")
    for row in students:
        print(row)


if __name__ == "__main__":
    main()