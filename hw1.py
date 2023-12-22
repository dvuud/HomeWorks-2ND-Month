# Задача 1
# class Student:
#     def __init__(self, name, surname, student_ticket ):
#         self.name = name
#         self.surname = surname
#         self.student_ticket = student_ticket
#         self.courses = []
        
#     def add_course(self, course):
#         if course not in self.courses:
#             self.courses.append(course)
#             print(f"{course} добавлен студенту {self.name} {self.surname}")
            
#     def delete_course(self, course):
#         if course in self.courses:
#             self.courses.remove(course)
#             print(f"{course} удален из списка студента {self.name} {self.surname}") 
            
#     def info_student(self):
#         print(f"Студент {self.name} {self.surname}")
#         print(f"Номер студентеческого билета {self.student_ticket}")
#         print("Посещаемые курсы")
#         for course in self.courses:
#             print(f"{course}")

# student = Student("Давуд", "Балтабаев", "34326")
# student.add_course("Английский")
# student.add_course("Математика")
# student.info_student()


# Задача 2

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, title, author):
#         book = Book(title, author)
#         self.books.append(book)

#     def remove_book(self, title):
#         self.books = [book for book in self.books if book.title != title]

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title == title and book.is_available:
#                 book.is_available = False
#                 return f"Книга '{title}' выдана"
#         return f"Книга '{title}' не доступна для выдачи"

#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title and not book.is_available:
#                 book.is_available = True
#                 return f"Книга '{title}' возвращена"
#         return f"Книга '{title}' не найдена в библиотеке или уже доступна"


# library = Library()
# library.add_book("Война и мир", "Лев Толстой")
# library.add_book("Преступление и наказание", "Федор Достоевский")

# print(library.borrow_book("Война и мир"))  
# print(library.borrow_book("Война и мир"))  
# print(library.return_book("Война и мир"))  


# Задача 3
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        
    def area(self):
        return self.side_length**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
square = Square(5)
triangle = Triangle(3, 7)

print("Площадь круга: ", circle.area())
print("Площадь квадрата: ", square.area())
print("Площадь треугольника:", triangle.area())