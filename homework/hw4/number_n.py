print("Добро пожаловать в программу, которая будет отображать количество введёных пользователем нулей")
n = int(input("Введите количестов вводимых чисел"))
zero = 0
a = 0
for i in range(1, n + 1):
    s = int(input("Введите целое число:"))
    if s == 0:
        a += 1
        print(a)
input()