print("Добро пожаловать в программу, которая сравнивает возможности инвесторов и выдаёт значениия в зависимости от введёных значений для сравнения.")
close = 0
while close != 1:
    X = int(input("Введите минмальную сумму инвестиций:"))
    B = int(input("Введите доступные средства Ивана:"))
    A = int(input("Введите доступные средства Майка:"))
    if A >= X and B >= X:
        print("2")
    elif A >= X and B < X:
        print("Mike")
    elif A < X and B >= X:
        print("Ivan")
    elif A + B >= X:
        print("1")
    else:
        print("0")
    close = int(input('Введите "1", если хотите закрыть программу или введите "0", ввести новые значения'))
