import csv
import hashlib
import time
import sys

## For student 
class Student:
    def __init__(self, email, first_name, last_name, course_id, grade, marks):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def display_records(self):
        """Print a single student's record in a readable format."""
        print(f"Email: {self.email}, Name: {self.first_name} {self.last_name}, "
              f"Course: {self.course_id}, Grade: {self.grade}, Marks: {self.marks}")

    @staticmethod
    def load_students():
        students = []
        try:
            with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_students.csv - Students.csv", "r", newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  
                for row in reader:
                    if row:
                        students.append(Student(*row))
        except FileNotFoundError:
            pass
        return students

    @staticmethod
    def save_students(students):
        with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_students.csv - Students.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Grade", "Marks"])
            for student in students:
                writer.writerow([student.email, student.first_name, student.last_name,
                                 student.course_id, student.grade, student.marks])

    @staticmethod
    def add_new_student(student):
        students = Student.load_students()
        for s in students:
            if s.email == student.email:
                print("Student already exists.")
                return
        students.append(student)
        Student.save_students(students)
        print("Student added successfully.")

    @staticmethod
    def search_student(email):
        start_time = time.time()
        students = Student.load_students()
        for s in students:
            if s.email == email:
                print(f"Searching took {time.time() - start_time:.4f} seconds")
                s.display_records()
                return
        print(f"Searching took {time.time() - start_time:.4f} seconds")
        print("Student not found.")

    @staticmethod
    def delete_student(email):
        students = Student.load_students()
        new_students = [s for s in students if s.email != email]
        if len(new_students) < len(students):
            Student.save_students(new_students)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    @staticmethod
    def update_student_record(email, new_first_name, new_last_name, new_course_id, new_grade, new_marks):
        students = Student.load_students()
        updated = False
        for s in students:
            if s.email == email:
                s.first_name = new_first_name
                s.last_name = new_last_name
                s.course_id = new_course_id
                s.grade = new_grade
                s.marks = new_marks
                updated = True
                break
        if updated:
            Student.save_students(students)
            print("Student record updated successfully.")
        else:
            print("Student not found.")

    @staticmethod
    def check_my_grades(email):
        students = Student.load_students()
        for s in students:
            if s.email == email:
                print(f"Grade for {s.first_name} {s.last_name} is: {s.grade}")
                return
        print("Student not found.")

    @staticmethod
    def check_my_marks(email):
        students = Student.load_students()
        for s in students:
            if s.email == email:
                print(f"Marks for {s.first_name} {s.last_name} are: {s.marks}")
                return
        print("Student not found.")

    @staticmethod
    def sort_students(by="marks"):
        students = Student.load_students()
        start_time = time.time()
        if by == "marks":
            students.sort(key=lambda s: int(s.marks))
        elif by == "name":
            students.sort(key=lambda s: s.first_name.lower())
        else:
            students.sort(key=lambda s: s.email.lower())
        Student.save_students(students)
        print(f"Sorting took {time.time() - start_time:.4f} seconds")
        print("Students have been sorted and saved.")

    @staticmethod
    def calculate_average():
        students = Student.load_students()
        if not students:
            print("No students available to calculate average.")
            return 0
        total = sum(int(s.marks) for s in students)
        average = total / len(students)
        print(f"Average marks: {average:.2f}")
        return average


## FOR Course Class 
class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description

    @staticmethod
    def load_courses():
        courses = []
        try:
            with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_courses.csv", "r", newline='') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if row:
                        courses.append(Course(*row))
        except FileNotFoundError:
            pass
        return courses

    @staticmethod
    def save_courses(courses):
        with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_courses.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Course ID", "Name", "Description"])
            for c in courses:
                writer.writerow([c.course_id, c.name, c.description])

    @staticmethod
    def add_new_course(course):
        courses = Course.load_courses()
        for c in courses:
            if c.course_id == course.course_id:
                print("Course already exists.")
                return
        courses.append(course)
        Course.save_courses(courses)
        print("Course added successfully.")

    @staticmethod
    def delete_course(course_id):
        courses = Course.load_courses()
        new_courses = [c for c in courses if c.course_id != course_id]
        if len(new_courses) < len(courses):
            Course.save_courses(new_courses)
            print("Course deleted successfully.")
        else:
            print("Course not found.")

    @staticmethod
    def update_course(course_id, new_name, new_description):
        courses = Course.load_courses()
        updated = False
        for c in courses:
            if c.course_id == course_id:
                c.name = new_name
                c.description = new_description
                updated = True
                break
        if updated:
            Course.save_courses(courses)
            print("Course updated successfully.")
        else:
            print("Course not found.")

    @staticmethod
    def display_courses():
        courses = Course.load_courses()
        if courses:
            print("Course List:")
            for c in courses:
                print(f"ID: {c.course_id}, Name: {c.name}, Description: {c.description}")
        else:
            print("No courses available.")

## fro professor class
class Professor:
    def __init__(self, email, name, rank, course_id):
        self.email = email
        self.name = name
        self.rank = rank
        self.course_id = course_id

    @staticmethod
    def load_professors():
        professors = []
        try:
            with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_professors.csv - Professors.csv", "r", newline='') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if row:
                        professors.append(Professor(*row))
        except FileNotFoundError:
            pass
        return professors

    @staticmethod
    def save_professors(professors):
        with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_professors.csv - Professors.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "Name", "Rank", "Course ID"])
            for p in professors:
                writer.writerow([p.email, p.name, p.rank, p.course_id])

    @staticmethod
    def add_new_professor(prof):
        professors = Professor.load_professors()
        for p in professors:
            if p.email == prof.email:
                print("Professor already exists.")
                return
        professors.append(prof)
        Professor.save_professors(professors)
        print("Professor added successfully.")

    @staticmethod
    def delete_professor(email):
        professors = Professor.load_professors()
        new_profs = [p for p in professors if p.email != email]
        if len(new_profs) < len(professors):
            Professor.save_professors(new_profs)
            print("Professor deleted successfully.")
        else:
            print("Professor not found.")

    @staticmethod
    def professors_details():
        professors = Professor.load_professors()
        if professors:
            print("Professor Details:")
            for p in professors:
                print(f"Email: {p.email}, Name: {p.name}, Rank: {p.rank}, Course ID: {p.course_id}")
        else:
            print("No professor details available.")

    @staticmethod
    def modify_professor_details(email, new_name, new_rank, new_course_id):
        professors = Professor.load_professors()
        updated = False
        for p in professors:
            if p.email == email:
                p.name = new_name
                p.rank = new_rank
                p.course_id = new_course_id
                updated = True
                break
        if updated:
            Professor.save_professors(professors)
            print("Professor details updated successfully.")
        else:
            print("Professor not found.")

    @staticmethod
    def show_course_details_by_professor(prof_email):
        professors = Professor.load_professors()
        for p in professors:
            if p.email == prof_email:
                course_id = p.course_id
                courses = Course.load_courses()
                for c in courses:
                    if c.course_id == course_id:
                        print(f"Professor {p.name} is associated with Course: ID: {c.course_id}, Name: {c.name}, Description: {c.description}")
                        return
                print("Course details not found for the professor.")
                return
        print("Professor not found.")

# for grades 
# The Grades we have taken from the Student CSV file.
class Grades:
    @staticmethod
    def display_grade_report():
        students = Student.load_students()
        if not students:
            print("No grade records available!")
            return
        # Group students by grade from the Student CSV file
        grade_dict = {}
        for s in students:
            try:
                marks = int(s.marks)
            except ValueError:
                marks = 0
            if s.grade not in grade_dict:
                grade_dict[s.grade] = []
            grade_dict[s.grade].append(marks)
        print("Grade Report:")
        for grade, marks in grade_dict.items():
            count = len(marks)
            avg_marks = sum(marks) / count if count > 0 else 0
            print(f"Grade: {grade} | Count: {count} | Average Marks: {avg_marks:.2f}")


# For login users 
class LoginUser:
    def __init__(self, email, password, role):
        self.email = email
        self.password = LoginUser.encrypt_password(password)
        self.role = role

    @staticmethod
    def encrypt_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def decrypt_password(hashed_password):
        return "Decryption not supported for SHA256 hashed passwords."

    @staticmethod
    def load_users():
        users = []
        try:
            with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_login.csv - Login Data.csv", "r", newline='') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if row:
                        user = LoginUser(row[0], row[1], row[2])
                        user.password = row[1]
                        users.append(user)
        except FileNotFoundError:
            pass
        return users

    @staticmethod
    def save_users(users):
        with open(r"/Users/kanikathapliyal/Desktop/SJSU/DATA-200/lab1_login.csv - Login Data.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "Password", "Role"])
            for user in users:
                writer.writerow([user.email, user.password, user.role])

    @staticmethod
    def register_user(email, password, role):
        users = LoginUser.load_users()
        for u in users:
            if u.email == email:
                print("User already registered.")
                return
        new_user = LoginUser(email, password, role)
        users.append(new_user)
        LoginUser.save_users(users)
        print("User registered successfully.")

    @staticmethod
    def check_login(email, password):
        users = LoginUser.load_users()
        hashed_input = LoginUser.encrypt_password(password)
        for user in users:
            if user.email == email and user.password == hashed_input:
                return f"Login successful as {user.role}"
        return "Invalid credentials"

    @staticmethod
    def change_password(email, old_password, new_password):
        users = LoginUser.load_users()
        hashed_old = LoginUser.encrypt_password(old_password)
        changed = False
        for user in users:
            if user.email == email and user.password == hashed_old:
                user.password = LoginUser.encrypt_password(new_password)
                changed = True
                break
        if changed:
            LoginUser.save_users(users)
            print("Password changed successfully.")
        else:
            print("Invalid email or password.")

    @staticmethod
    def logout():
        print("User logged out successfully.")

# unit test cases 

import unittest 
import tempfile
import os
from io import StringIO

class TestStudentOperations(unittest.TestCase):
    def setUp(self):
        
        self.temp_student_file = tempfile.NamedTemporaryFile(delete=False, mode="w+", newline="", suffix=".csv")
        self.temp_student_file.write("Email,First Name,Last Name,Course ID,Grade,Marks\n")
        self.temp_student_file.flush()
        
        self.orig_load = Student.load_students
        self.orig_save = Student.save_students
        Student.load_students = staticmethod(lambda: self._load_students())
        Student.save_students = lambda students: self._save_students(students)
    
    def tearDown(self):
        Student.load_students = self.orig_load
        Student.save_students = self.orig_save
        os.remove(self.temp_student_file.name)
    
    def _load_students(self):
        students = []
        with open(self.temp_student_file.name, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    students.append(Student(*row))
        return students
    
    def _save_students(self, students):
        with open(self.temp_student_file.name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Grade", "Marks"])
            for student in students:
                writer.writerow([student.email, student.first_name, student.last_name,
                                 student.course_id, student.grade, student.marks])
    
    def test_add_update_delete_student(self):
        # Add a student
        s = Student("test@sjsu.edu", "Test", "User", "C001", "A", "85")
        Student.add_new_student(s)
        students = Student.load_students()
        self.assertTrue(any(st.email == "test@sjsu.edu" for st in students))
        
        # Update the student record
        Student.update_student_record("test@sjsu.edu", "Updated", "User", "C002", "A+", "90")
        students = Student.load_students()
        for st in students:
            if st.email == "test@sjsu.edu":
                self.assertEqual(st.first_name, "Updated")
                self.assertEqual(st.course_id, "C002")
                self.assertEqual(st.marks, "90")
        
        # Delete the student
        Student.delete_student("test@sjsu.edu")
        students = Student.load_students()
        self.assertFalse(any(st.email == "test@sjsu.edu" for st in students))
    
    def test_search_timing(self):
        s = Student("search@sjsu.edu", "Search", "User", "C001", "B", "75")
        Student.add_new_student(s)
        captured_output = StringIO()
        sys.stdout = captured_output
        Student.search_student("search@sjsu.edu")
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("search@sjsu.edu", output)
        self.assertIn("Searching took", output)
    
    def test_sorting_and_average(self):

        students_to_add = [
            Student("a@sjsu.edu", "A", "User", "C001", "A", "90"),
            Student("b@sjsu.edu", "B", "User", "C001", "B", "70"),
            Student("c@sjsu.edu", "C", "User", "C001", "C", "80")
        ]
        for s in students_to_add:
            Student.add_new_student(s)
        # Test sorting by name
        Student.sort_students(by="name")
        sorted_students = Student.load_students()
        names = [s.first_name for s in sorted_students]
        self.assertEqual(names, sorted(names, key=lambda n: n.lower()))
        # Test sorting by marks
        Student.sort_students(by="marks")
        sorted_students = Student.load_students()
        marks = [int(s.marks) for s in sorted_students]
        self.assertEqual(marks, sorted(marks))
        # Test average calculation
        avg = Student.calculate_average()
        expected_avg = (90 + 70 + 80) / 3
        self.assertAlmostEqual(avg, expected_avg)

class TestCourseOperations(unittest.TestCase):
    def setUp(self):
        self.temp_course_file = tempfile.NamedTemporaryFile(delete=False, mode="w+", newline="", suffix=".csv")
        self.temp_course_file.write("Course ID,Credits,Name,Description\n")
        self.temp_course_file.flush()
        self.orig_load = Course.load_courses
        self.orig_save = Course.save_courses
        Course.load_courses = staticmethod(lambda: self._load_courses())
        Course.save_courses = lambda courses: self._save_courses(courses)
    
    def tearDown(self):
        Course.load_courses = self.orig_load
        Course.save_courses = self.orig_save
        os.remove(self.temp_course_file.name)
    
    def _load_courses(self):
        courses = []
        with open(self.temp_course_file.name, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    courses.append(Course(*row))
        return courses
    
    def _save_courses(self, courses):
        with open(self.temp_course_file.name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Course ID", "Name", "Description"])
            for c in courses:
                writer.writerow([c.course_id, c.name, c.description])
    
    def test_add_delete_update_course(self):
        # Add course
        c = Course("C001", "3", "Math", "Algebra")
        Course.add_new_course(c)
        courses = Course.load_courses()
        self.assertTrue(any(course.course_id == "C001" for course in courses))
        
        # Update course
        Course.update_course("C001", "4", "Advanced Math", "Advanced Algebra")
        courses = Course.load_courses()
        for course in courses:
            if course.course_id == "C001":
                self.assertEqual(course.name, "Advanced Math")
                self.assertEqual(course.description, "Advanced Algebra")
        
        # Delete course
        Course.delete_course("C001")
        courses = Course.load_courses()
        self.assertFalse(any(course.course_id == "C001" for course in courses))

class TestProfessorOperations(unittest.TestCase):
    def setUp(self):
        self.temp_prof_file = tempfile.NamedTemporaryFile(delete=False, mode="w+", newline="", suffix=".csv")
        self.temp_prof_file.write("Email,Name,Rank,Course ID\n")
        self.temp_prof_file.flush()
        self.orig_load = Professor.load_professors
        self.orig_save = Professor.save_professors
        Professor.load_professors = staticmethod(lambda: self._load_professors())
        Professor.save_professors = lambda profs: self._save_professors(profs)
    
    def tearDown(self):
        Professor.load_professors = self.orig_load
        Professor.save_professors = self.orig_save
        os.remove(self.temp_prof_file.name)
    
    def _load_professors(self):
        professors = []
        with open(self.temp_prof_file.name, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    professors.append(Professor(*row))
        return professors
    
    def _save_professors(self, professors):
        with open(self.temp_prof_file.name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "Name", "Rank", "Course ID"])
            for p in professors:
                writer.writerow([p.email, p.name, p.rank, p.course_id])
    
    def test_add_delete_update_professor(self):
        # Add professor
        p = Professor("prof@sjsu.edu", "Prof. Smith", "Senior", "C001")
        Professor.add_new_professor(p)
        professors = Professor.load_professors()
        self.assertTrue(any(prof.email == "prof@sjsu.edu" for prof in professors))
        
        # Update professor
        Professor.modify_professor_details("prof@sjsu.edu", "Prof. John Smith", "Head", "C002")
        professors = Professor.load_professors()
        for prof in professors:
            if prof.email == "prof@sjsu.edu":
                self.assertEqual(prof.name, "Prof. John Smith")
                self.assertEqual(prof.rank, "Head")
                self.assertEqual(prof.course_id, "C002")
        
        # Delete professor
        Professor.delete_professor("prof@sjsu.edu")
        professors = Professor.load_professors()
        self.assertFalse(any(prof.email == "prof@sjsu.edu" for prof in professors))


## time functions
def test_course_operations():
    print("\n Timing Test: Course Operations")
    start_time = time.time()
    try:
        Course.add_new_course(Course("DATA200", "Python", "Advanced topics in python for data science"))
        print(f"Time to add a course: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during course addition:", e)

    start_time = time.time()
    try:
        Course.update_course("DATA200", "Machine Learning", "Deep Dive into ML")
        print(f"Time to modify a course: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during course modification:", e)

    start_time = time.time()
    try:
        Course.delete_course("DATA200")
        print(f"Time to delete a course: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during course deletion:", e)


def test_professor_operations():
    print("\n Timing Test: Professor Operations ")
    start_time = time.time()
    try:
        Professor.add_new_professor(Professor("john@sjsu.edu", "John Doe", "Senior Professor", "DATA202"))
        print(f"Time to add a professor: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during professor addition:", e)

    start_time = time.time()
    try:
        Professor.modify_professor_details("john@sjsu.edu", "Jane Doe", "Head Professor", "DATA202")
        print(f"Time to modify a professor: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during professor modification:", e)

    start_time = time.time()
    try:
        Professor.delete_professor("john@sjsu.edu")
        print(f"Time to delete a professor: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during professor deletion:", e)


def test_student_operations():
    print("\n Timing Test: Student Operations ")
    start_time = time.time()
    try:
        for i in range(1000):
            Student.add_new_student(Student(f"student{i}@sjsu.edu",
                                           f"Student{i}",
                                           "Test",
                                           "C001",
                                           "A",
                                           "80"))
        print(f"Time to add 1000 students: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during student addition:", e)

    start_time = time.time()
    try:
        Student.update_student_record("student500@sjsu.edu",
                                     "NewName",
                                     "Updated Student",
                                     "C001",
                                     "A+",
                                     "90")
        print(f"Time to modify a student: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during student modification:", e)

    start_time = time.time()
    try:
        Student.delete_student("student500@sjsu.edu")
        print(f"Time to delete a student: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during student deletion:", e)


def test_search_functionality():
    print("\n Timing Test: Search Functionality ")
    start_time = time.time()
    try:
        Student.search_student("student100@sjsu.edu")
        print(f"Time to search for a student: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during student search:", e)


def test_sorting_functionality():
    print("\n Timing Test: Sorting Functionality ")
    start_time = time.time()
    try:
        students = Student.load_students()
        students.sort(key=lambda s: int(s.marks))
        print(f"Time to sort students by marks: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during sorting by marks:", e)

    start_time = time.time()
    try:
        students = Student.load_students()
        students.sort(key=lambda s: s.email.lower())
        print(f"Time to sort students by email: {time.time() - start_time:.4f} seconds")
    except Exception as e:
        print("Error during sorting by email:", e)


def run_unit_tests():
    """
    measuring time for each operation 
    """
    print("\n=== Running Timing Unit Tests ===")
    test_course_operations()
    test_professor_operations()
    test_student_operations()
    test_search_functionality()
    test_sorting_functionality()
    print("\nAll timing tests completed.")


#  Interactive Menu for checking my grades
def main_menu():
    while True:
        print("\nMenu:")
        print("1.  Register User")
        print("2.  Login User")
        print("3.  Logout User")
        print("4.  Change Password")
        print("5.  Add Student")
        print("6.  Search Student")
        print("7.  Update Student Record")
        print("8.  Delete Student")
        print("9.  Check My Grades (Student)")
        print("10. Check My Marks (Student)")
        print("11. Sort Students by Marks")
        print("12. Sort Students by Name")
        print("13. Calculate Average Marks")
        print("14. Add Course")
        print("15. Display Courses")
        print("16. Delete Course")
        print("17. Update Course")
        print("18. Add Professor")
        print("19. Display Professor Details")
        print("20. Modify Professor Details")
        print("21. Delete Professor")
        print("22. Show Course Details by Professor")
        print("23. Display Grade Report")
        print("24. Run Unit Tests")
        print("25. Exit")
    
        choice = input("Enter your choice: ").strip()
    
        if choice == "1":
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            role = input("Enter user role: ")
            LoginUser.register_user(email, password, role)
    
        elif choice == "2":
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            result = LoginUser.check_login(email, password)
            print(result)
    
        elif choice == "3":
            LoginUser.logout()
    
        elif choice == "4":
            email = input("Enter user email: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            LoginUser.change_password(email, old_password, new_password)
    
        elif choice == "5":
            email = input("Enter student email: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            course_id = input("Enter course ID: ")
            grade = input("Enter grade: ")
            marks = input("Enter marks: ")
            Student.add_new_student(Student(email, first_name, last_name, course_id, grade, marks))
    
        elif choice == "6":
            email = input("Enter student email to search: ")
            Student.search_student(email)
    
        elif choice == "7":
            email = input("Enter student email to update: ")
            new_first = input("Enter new first name: ")
            new_last = input("Enter new last name: ")
            new_course = input("Enter new course ID: ")
            new_grade = input("Enter new grade: ")
            new_marks = input("Enter new marks: ")
            Student.update_student_record(email, new_first, new_last, new_course, new_grade, new_marks)
    
        elif choice == "8":
            email = input("Enter student email to delete: ")
            Student.delete_student(email)
    
        elif choice == "9":
            email = input("Enter student email to check grade: ")
            Student.check_my_grades(email)
    
        elif choice == "10":
            email = input("Enter student email to check marks: ")
            Student.check_my_marks(email)
    
        elif choice == "11":
            Student.sort_students(by="marks")
    
        elif choice == "12":
            Student.sort_students(by="name")
    
        elif choice == "13":
            Student.calculate_average()
    
        elif choice == "14":
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            description = input("Enter course description: ")
            Course.add_new_course(Course(course_id, name, description))
    
        elif choice == "15":
            Course.display_courses()
    
        elif choice == "16":
            course_id = input("Enter course ID to delete: ")
            Course.delete_course(course_id)
    
        elif choice == "17":
            course_id = input("Enter course ID to update: ")
            name = input("Enter new course name: ")
            description = input("Enter new description: ")
            Course.update_course(course_id, name, description)
    
        elif choice == "18":
            email = input("Enter professor email: ")
            name = input("Enter professor name: ")
            rank = input("Enter professor rank: ")
            course_id = input("Enter professor's course ID: ")
            Professor.add_new_professor(Professor(email, name, rank, course_id))
    
        elif choice == "19":
            Professor.professors_details()
    
        elif choice == "20":
            email = input("Enter professor email to modify: ")
            new_name = input("Enter new professor name: ")
            new_rank = input("Enter new rank: ")
            new_course_id = input("Enter new course ID: ")
            Professor.modify_professor_details(email, new_name, new_rank, new_course_id)
    
        elif choice == "21":
            email = input("Enter professor email to delete: ")
            Professor.delete_professor(email)
    
        elif choice == "22":
            prof_email = input("Enter professor email to show course details: ")
            Professor.show_course_details_by_professor(prof_email)
    
        elif choice == "23":
            Grades.display_grade_report()
    
        elif choice == "24":
            run_unit_tests()
    
        elif choice == "25":
            print("Exiting program.")
            break
    
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # If test is passed as an argumen then run unittest module else run the interactive menu.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        main_menu()
