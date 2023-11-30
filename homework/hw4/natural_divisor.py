exit = ""
while exit.lower() != "n":
    x = abs(int(input("Введите натуральное число, делители которого вы хотите найти\n>>>")))
    ask = input("\nПоказать делители? (Y/N)\n>>>")
    divisor_cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            divisor = x // i 
            divisor_cnt += 1
            if ask.lower() == "y":
                print(divisor)
                
    exit = input(f"Количество делителей:\n>>>{divisor_cnt}\nНачать заново? (Y/N)\n>>>")
    