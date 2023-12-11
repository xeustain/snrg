print("Введите числа первого списка (ввод завершите пустой строкой):")
input_str1 = input()
set1 = set()

while input_str1:
    try:
        num = int(input_str1)
        set1.add(num)
    except ValueError:
        print("Некорректный ввод числа. Пожалуйста, введите целое число.")
    input_str1 = input()

print("Введите числа второго списка (ввод завершите пустой строкой):")
input_str2 = input()
set2 = set()

while input_str2:
    try:
        num = int(input_str2)
        set2.add(num)
    except ValueError:
        print("Некорректный ввод числа. Пожалуйста, введите целое число.")
    input_str2 = input()

intersection_set = set1.intersection(set2)
cnt_intersection_set = len(intersection_set)

print(f"Количество общих чисел: {cnt_intersection_set}")
print("Общие числа:", *intersection_set)
input()
