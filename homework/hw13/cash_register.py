
class CashRegister:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount


    def top_up(self, x):
        self.amount += x


    def count_1000(self):
        return self.amount // 1000


    def take_away(self, x):
        if self.amount < x:
            raise ValueError("Недостаточно средств в кассе")
        else:
            self.amount -= x


    def get_amount(self):
        return self.amount


    def set_amount(self, new_amount):
        self.amount = new_amount


cash_register = CashRegister(0)

while True:
    print("\nВыберите действие:")
    print("1. Внести деньги")
    print("2. Вывести текущий баланс")
    print("3. Посчитать количество целых тысяч")
    print("4. Взять деньги")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        amount_to_add = int(input("Введите сумму для пополнения: "))
        cash_register.top_up(amount_to_add)
        print("Деньги успешно внесены")

    elif choice == "2":
        print("Текущий баланс: ", cash_register.get_amount())

    elif choice == "3":
        print("Количество целых тысяч: ", cash_register.count_1000())

    elif choice == "4":
        amount_to_take = int(input("Введите сумму для изъятия: "))
        try:
            cash_register.take_away(amount_to_take)
            print("Деньги успешно изъяты")
        except ValueError as e:
            print(e)

    elif choice == "5":
        print("Работа с кассой завершена")
        break


    else:
        print("Некорректный ввод. Пожалуйста, введите число от 1 до 5.")
