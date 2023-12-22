import random 


class SlotMachine:
    def __init__(self, name):
        self.name = name
        self.user_balance = 100 
        self.game_balance = 0
    
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Ваш баланс: {self.user_balance}")
        print(f"Ваш игровой баланс: {self.game_balance}")
        
    def balance_up(self, addition):
        if addition > 100:
            print("Ты можешь пополнять только до 100 долларов")
        else:
            self.user_balance -= addition
            self.game_balance += addition
            
    def top_up_balance(self, addition):
        self.balance_up(addition)
        
        
    def game(self):
        s_num = random.randint(1,10)
        attempts = 5
        
        while attempts > 0:
            my_num = int(input("""Напишите число от 1 - 10
    (у вас 5 попыток): """))
            if my_num == s_num:
                self.game_balance += 50
                print("Поздравляю вы выиграли 50$")
                break
            else:
                print("Неправильный ответ ): попробуйте заново")
                attempts -= 1
                self.user_balance -= 10
    
    def conclusion(self, addition):
        if addition >= 50:
            self.user_balance -= addition 
        else:
            print("Вы можете вывеcти только oт 50$")
            
    def main(self):
        command = int(input("Введите команду с 1 - 4: "))
        if command == 1:
            print(self.info())
        elif command == 2:
            going_up_balance = int(input("Введите сумму для увеличения баланс: "))
            self.balance_up(going_up_balance)
            self.info()
        elif command == 3:
            self.game()
            self.info()
        elif command == 4:
            addition = int(input("Введите сумму для вывода: "))
            self.conclusion(addition)
            self.info()
        else:
            print("Неправильно введенная команда, попробуйте еще!")


slotmachine = SlotMachine("Dava")
slotmachine.main()
