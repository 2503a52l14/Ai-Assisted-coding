class StudentRecord:
    def __init__(self, name, student_id, courses=None):
        self.studentName = name
        self.student_id = student_id
        self.courses = courses if courses is not None else []  # ✅ Safe default list

    def add_course(self, course):
        self.courses.append(course)

    def get_summary(self):
        return f"Student: {self.studentName}, ID: {self.student_id}, Courses: {', '.join(self.courses)}"


class Department:
    def __init__(self, deptName, students=None):
        self.dept_name = deptName
        self.students = students if students is not None else []  # ✅ Initialize properly

    def enroll_student(self, student):
        self.students.append(student)

    def department_summary(self):
        return f"Department: {self.dept_name}, Total Students: {len(self.students)}"  # ✅ Fixed attribute


# ✅ Testing
s1 = StudentRecord("Alice", 101, ["Math", "Science"])
d1 = Department("Computer Science")
d1.enroll_student(s1)

print(s1.get_summary())          # Student: Alice, ID: 101, Courses: Math, Science
print(d1.department_summary())   # Department: Computer Science, Total Students: 1