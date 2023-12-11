a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

dict = {}
for i in range(a, b + 1):
    dict[i] = i ** i


print(dict)
input()
