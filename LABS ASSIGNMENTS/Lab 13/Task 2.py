class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"Student[ID={self.student_id}, Name={self.name}, Age={self.age}]"

class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, student_id):
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(name, age, student_id)

    def remove_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        del self.students[student_id]

    def get_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        return self.students[student_id]

    def list_students(self):
        return list(self.students.values())

def main():
    management = StudentManagement()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Student")
        print("4. List All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                student_id = input("Enter student ID: ")
                management.add_student(name, age, student_id)
                print("Student added successfully.")

            elif choice == 2:
                student_id = input("Enter student ID to remove: ")
                management.remove_student(student_id)
                print("Student removed successfully.")

            elif choice == 3:
                student_id = input("Enter student ID to view: ")
                student = management.get_student(student_id)
                print(student)

            elif choice == 4:
                students = management.list_students()
                for student in students:
                    print(student)

            elif choice == 5:
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()