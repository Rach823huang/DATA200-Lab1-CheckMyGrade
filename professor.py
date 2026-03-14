from file_manager import read_csv_file, append_csv_file, write_csv_file


class Professor:
    def __init__(self, professor_id, name, email_address, rank, course_id):
        self.professor_id = professor_id
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

    def to_list(self):
        return [
            self.professor_id,
            self.name,
            self.email_address,
            self.rank,
            self.course_id
        ]

    def display_record(self):
        print(
            f"Professor ID: {self.professor_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email_address}, "
            f"Rank: {self.rank}, "
            f"Course ID: {self.course_id}"
        )

    @staticmethod
    def add_new_professor():
        professor_id = input("Enter professor ID: ")
        name = input("Enter professor name: ")
        email_address = input("Enter professor email: ")
        rank = input("Enter professor rank: ")
        course_id = input("Enter course ID: ")

        professor = Professor(professor_id, name, email_address, rank, course_id)
        append_csv_file("professor.csv", professor.to_list())
        print("Professor added successfully.")

    @staticmethod
    def display_all_professors():
        professors = read_csv_file("professor.csv")
        if not professors:
            print("No professor records found.")
            return

        print("\nProfessor Records:")
        for row in professors:
            print(row)

    @staticmethod
    def delete_professor(professor_id_to_delete):
        professors = read_csv_file("professor.csv")
        updated_professors = []
        found = False

        for row in professors:
            if row[0] != professor_id_to_delete:
                updated_professors.append(row)
            else:
                found = True

        if found:
            header = ["professor_id", "name", "email_address", "rank", "course_id"]
            write_csv_file("professor.csv", header, updated_professors)
            print("Professor deleted successfully.")
        else:
            print("Professor not found.")

    @staticmethod
    def update_professor(professor_id_to_update):
        professors = read_csv_file("professor.csv")
        updated_professors = []
        found = False

        for row in professors:
            if row[0] == professor_id_to_update:
                found = True
                print("Enter new values for the professor:")
                new_professor_id = input("Enter new professor ID: ")
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                new_rank = input("Enter new rank: ")
                new_course_id = input("Enter new course ID: ")

                updated_professors.append([
                    new_professor_id,
                    new_name,
                    new_email,
                    new_rank,
                    new_course_id
                ])
            else:
                updated_professors.append(row)

        if found:
            header = ["professor_id", "name", "email_address", "rank", "course_id"]
            write_csv_file("professor.csv", header, updated_professors)
            print("Professor updated successfully.")
        else:
            print("Professor not found.")