import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255),
    age INTEGER,
    bio TEXT,
    balance INTEGER,
    wallet_id VARCHAR(16),
    email VARCHAR(255)
    )''')

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.bio = None
        self.balance = 0
        self.wallet_id = None
        self.email = None

    def register(self, name, surname, age, email, bio):
        self.name = name
        self.surname = surname
        self.age = age
        self.bio = bio
        self.email = email
        cursor.execute(f'''INSERT INTO clients(name, surname, age, bio, balance, wallet_id, email) VALUES 
                          ('{self.name}', '{self.surname}', {self.age}, '{self.bio}', {self.balance}, '1234765498242567', '{self.email}')''')
        connect.commit()

    def deposit(self, amount):
        cursor.execute(f'''UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}' ''')
        connect.commit()
        self.balance += amount
        print(f"Уважаемый {self.name} {self.surname}, вы успешно пополнили баланс !!!")
        print("=====================================================================")

    def vyvod(self, money):
        cursor.execute(f'''UPDATE clients SET balance = balance - {money} WHERE email = '{self.email}' ''')
        connect.commit()
        self.balance -= money
        if money >= 50:
            print(f"Уважаемый {self.name} {self.surname} вы успешно вывели деньги из баланса")
        else:
            print(f"Уважаемый {self.name} {self.surname} у вас не достаточно средств на балансе!!!")

    def view(self):
        cursor.execute('''SELECT * FROM clients''')
        clients = cursor.fetchall()
        for client in clients:
            print(client)
        connect.commit()

    def main(self):
        while True:
            commands = int(input("""
1 - Регистрация 
2 - Информация 
3 - Пополнить 
4 - Вывести 
5 - Выйти: """))
            if commands == 1:
                print("=========================================================")
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите свой возраст: "))
                bio = input("Введите свою биографию: ")
                email = input("Введите свою почту(example@gmail.com): ")
                print(f"Поздравляю {name}, вы успешно зарегистрировались ")
                print("=========================================================")
                if "@gmail.com" in email:
                    if age >= 17:
                        self.register(name, surname, age, email, bio)
                        print(f" Уважаемый {name} {surname}, вы прошли регистрацию !!")
                        print("=================================================")
                    else:
                        print(f"Уважаемый {name} {surname}, вам еще не исполнилось 17 лет!!!")
                else:
                    continue

            elif commands == 2:
                self.view()
                print("=====================================================")

            elif commands == 3:
                moneyy = int(input("Введите сумму пополнения: "))
                self.deposit(moneyy)

            elif commands == 4:
                babki = int(input("Введите сумму для вывода: "))
                self.vyvod(babki)
                
            elif commands == 5:
                break
                
            
bank = Bank()
bank.main()