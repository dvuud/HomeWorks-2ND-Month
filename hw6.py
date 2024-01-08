import sqlite3

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")

def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        print(book)

    conn.close()

def add_book(title, author, year):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('INSERT INTO books(title, author, year) VALUES (?,?,?)', (title, author, year))
    print("Ваша книга успешно добавлена!")

    conn.commit()
    conn.close()

def up_book(id, title, author, year):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('UPDATE books SET title=?, author=?, year=? WHERE id=?', (title, author, year, id))
    print("Ваша книга обновлена!")

    conn.commit()
    conn.close()

def delete_book(title):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('DELETE FROM books WHERE title=?', (title,))
    print("Книга удалена!")

    conn.commit()
    conn.close()

def main():
    while True:
        print("1. Посмотреть все книги")
        print("2. Добавить книгу")
        print("3. Что бы обновить информацию о книге")
        print("4. Что бы удалить книгу")
        choice = int(input("Выберите число от 1-4: "))

        if choice == 1:
            view_books()
            print("Все книги в библиотеке")

        elif choice == 2:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год выпуска книги: "))
            new_book = Book(title, author, year)
            add_book(new_book.title, new_book.author, new_book.year)

        elif choice == 3:
            id = int(input("Введите ID книги, чтобы обновить: "))
            author = input("Введите нового автора книги: ")
            title = input("Введите новое название книги: ")
            year = int(input("Введите новый год выпуска книги: "))
            up_book(id, title, author, year)

        elif choice == 4:
            title = input("Введите название книги, чтобы удалить: ")
            delete_book(title)
            break

        else:
            print("Неправильно введенная команда, повторите еще раз!")

if __name__ == "__main__":
    main()