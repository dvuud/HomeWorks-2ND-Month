import sqlite3

conn = sqlite3.connect("car_service.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY,
        number INTEGER,
        brand TEXT,
        model TEXT,
        year INTEGER,
        description TEXT,
        status_service TEXT DEFAULT 'На обслуживании'
    )
;''')

conn.commit()
conn.close()

def add_car(number, brand, model, year, description):
    conn = sqlite3.connect("car_service.db")
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO cars (number, brand, model, year, description) VALUES (?, ?, ?, ?, ?)',
                   (number, brand, model, year, description))
    
    print("Ваша машина успешно добавлена")
    
    conn.commit()
    conn.close()

# def up_cars(id, number, brand, model, description, year, status_service):
#     conn = sqlite3.connect("car_service.db")
#     cursor = conn.cursor()
    
def update_cars(id, number, brand, model, description, year, status_service):
    connect = sqlite3.connect('car_service.db')
    cursor = connect.cursor()
    cursor.execute('''
        UPDATE cars SET number=?,brand=?, model=?, year=?, description=?, status_service=? WHERE id=?
    ''', (number,brand, model, year, description, status_service, id))
    connect.commit()

def all_cars():
    connect = sqlite3.connect('car_service.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM cars WHERE status_service="На обслуживании"')
    cars = cursor.fetchall()
    connect.close()
    return cars


def view_ready_cars():
    conn = sqlite3.connect("car_service.db")
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM cars WHERE status_service = "Готово к выдаче"')
    
    cars = cursor.fetchall()
    
    for car in cars:
        print(car)
        
    conn.commit()
    conn.close()
    
def main():
    
    while True:
        print("1. Добавить машину на обслуживание")
        print("2. Обновить информацию об автомобиле")
        print("3. Просмотреть список автомобилей на обслуживании")
        print("4. Просмотреть список автомобилей, готовых к выдаче")

        choice = int(input("Введите команду от 1-4: "))

        if choice == 1:
            brand = input("Введите марку машины: ")
            model = input("Введите модель машины: ")
            year = int(input("Введите год машины: "))
            description = input("Введите описание работ: ")
            number = int(input("Введите номер машины: "))
            add_car(number, brand, model, year, description)
            
        elif choice == 2:
            id = int(input("Введите ID машинын: "))
            brand = input("Введите марку авто: ")
            model = input("Введите модель авто: ")
            year = int(input("Введите год машины: "))
            number = int(input("Введите номер машины: "))
            description = input("Введите описание работ: ")
            status_service = input("Введите статус вашей машины: ")
            update_cars(id, brand, model, year, number, description, status_service)
            
        elif choice == 3:
            cars = all_cars()
            print("Список автомобилей на обслуживании:")
            for car in cars:
                print(car)
        elif choice == 4:
            view_ready_cars()
            break
        else:
            print("Не правильно введенная команда, повторите заново!")
main()