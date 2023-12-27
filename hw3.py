class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def login(self, enter_password, enter_email):
        if enter_password == self.password and enter_email == self.email:
            print("Добро пожаловать!")
        else:
            print("Пароль или эл.почта не правильно введена, повторите попытку")

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password, student_id)
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        if course not in self.courses_enrolled:
            self.courses_enrolled.append(course)
            print(f"{course}, добавлен в {self.courses_enrolled}")

    def remove_course(self, course):
        if course in self.courses_enrolled:
            self.courses_enrolled.remove(course)
        print(f"{course}, удален из {self.courses_enrolled}")

class Teacher(User):
    def __init__(self, name, email, password, teacher_id):
        super().__init__(name, email, password, teacher_id)
        self.tch_courses = []

    def add_course(self, course):
        self.tch_courses.append(course)

    def assign_grade(self, student, grade, course):
        print(f"Учитель {self.name} поставил оценку ученику {student} оценка {grade} курс {course}")

class Admin(User):
    def __init__(self, name, email, password, admin_id):
        super().__init__(name, email, password, admin_id)
        self.admin_new_course = []

    def create_course(self, new_course):
        self.admin_new_course.append(new_course)
        print(f"Админ {self.name} создал новый курс {new_course}")

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, email, password, student_id, teacher_id):
        Student.__init__(self, name, email, password, student_id)
        Teacher.__init__(self, name, email, password, teacher_id)

student = Student("Davud", "davabalta@gmail.com", "dava0909", "3642")
teacher = Teacher("Владимир", "vladimir@gmail", "vld45628", "3252")
admin = Admin("admin", "admin@gmail.com", "admin2837", "A324")
teachingassistant = TeachingAssistant("Дима", "dima@gmail.com", "dd49389", "2432", "434")