a = 0
b = 0
while a >= b:
    a = abs(int(input("Введите значение A\n>>>")))
    b = abs(int(input("Введите значение B\n>>>")))
    if a >= b:
        print("Значение A не может быть больше B")
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)
input()