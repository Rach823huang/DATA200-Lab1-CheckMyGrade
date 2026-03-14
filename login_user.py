import base64
from file_manager import read_csv_file, append_csv_file


class LoginUser:
    def __init__(self, user_id, password, role):
        self.user_id = user_id
        self.password = password
        self.role = role

    def to_list(self):
        encrypted_password = self.encrypt_password(self.password)
        return [self.user_id, encrypted_password, self.role]

    @staticmethod
    def encrypt_password(password):
        encoded_bytes = base64.b64encode(password.encode("utf-8"))
        return encoded_bytes.decode("utf-8")

    @staticmethod
    def decrypt_password(encoded_password):
        decoded_bytes = base64.b64decode(encoded_password.encode("utf-8"))
        return decoded_bytes.decode("utf-8")

    @staticmethod
    def add_new_login_user():
        user_id = input("Enter user ID: ")
        password = input("Enter password: ")
        role = input("Enter role (student/professor/admin): ")

        user = LoginUser(user_id, password, role)
        append_csv_file("login.csv", user.to_list())
        print("Login user added successfully.")

    @staticmethod
    def display_all_login_users():
        users = read_csv_file("login.csv")
        if not users:
            print("No login records found.")
            return

        print("\nLogin Records:")
        for row in users:
            print(row)

    @staticmethod
    def login():
        entered_user_id = input("Enter user ID: ")
        entered_password = input("Enter password: ")

        users = read_csv_file("login.csv")

        for row in users:
            stored_user_id = row[0]
            stored_encrypted_password = row[1]
            stored_role = row[2]

            decrypted_password = LoginUser.decrypt_password(stored_encrypted_password)

            if stored_user_id == entered_user_id and decrypted_password == entered_password:
                print(f"Login successful. Welcome, {stored_user_id} ({stored_role})")
                return

        print("Invalid user ID or password.")