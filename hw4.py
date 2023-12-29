from abc import ABC, abstractmethod

class GeeksPeople(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def __str__(self):
        pass
    
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study
    
    def study(self):
        return f"{self.name}, учиться в группе {self.group_where_study}"
    
    def __str__(self):
        return f"Студент {self.name},айди студента {self.student_id}"
    
class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach
    
    def teach(self):
        return f"{self.name}, преподает в группе {self.group_where_teach}"
    
    def __str__(self):
        return f"Учитель {self.name}, айди учителя {self.teacher_id}"
    
class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id
    
    def create_group(self):
        return f"{self.name} создал новую группу"
    
    def __str__(self):
        return f"Admin: {self.name}, Id: {self.admin_id}"
    
class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)
        
student = Student("Давуд", "dava@gmail.com", "996738436", "S348", "14-1b")
teacher = Teacher("Alex", "alex@gmail.com", "43623277", "T326", "14-1b")
admin = Admin("Admin", "admin@gmail.com", "84378239", "A000")
mentor = Mentor("Valeriy", "valeriy@gmail.com", "732462", "S322", "17-2A", "722", "12-6A")

print(student)
print(student.study())

print(teacher)
print(teacher.teach())

print(admin)
print(admin.create_group())

print(mentor)
print(mentor.study())
print(mentor.teach())
    