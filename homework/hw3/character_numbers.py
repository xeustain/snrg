input("Добро пожаловать в программу, которая может описать число!\nЧтобы продолжить нажмите Enter...")
close = "работает"
while close.lower() != "выход":
    if close.lower() == "Выход":
        break
    x = int(input("Введите число\n\t>>>"))
    if x % 2 == 0 and x > 0:
        print("Число", x, "является ПОЛОЖИТЕЛЬНЫМ ЧЁТНЫМ!")
    elif x == 0:
        print("Число РАВНО НУЛЮ!")
    elif x % 2 == 0 and x < 0:
        print("Число", x, "является ОТРИЦАТЕЛЬНЫМ ЧЁТНЫМ!")
    elif x % 2 != 0 and x < 0:
        print("Число", x, "является ОТРИЦАТЕЛЬНЫМ НЕЧЁТНЫМ!")
    else:
        print("Число", x, "является ПОЛОЖИТЕЛЬНЫМ НЕЧЁТНЫМ!")
    close = input("Нажмите 'Enter', чтобы ввести новое число либо напишите 'Выход' для завершения программы\n>>>")