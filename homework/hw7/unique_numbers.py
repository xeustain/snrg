def get_piece_form(N, variant = 1):
    if 11 <= N % 100 <= 14:
        return "разных" if variant == 2 else "чисел"
    elif N % 10 == 1:
        return "разное" if variant == 2 else "число"
    elif 2 <= N % 10 <= 4:
        return "разных" if variant == 2 else "числа"
    else:
        return "разных" if variant == 2 else "чисел"
ok = 0

numbers = set()

while ok == 0:
    try:
        N = max(1, min(100000, int(input("Введите число в диапазоне 1 до 100000:\n"))))
    except ValueError:
        print('Некорректный ввод числа')
    else:
        ok = 1

while len(numbers) != N:
    try:
        user_input = input(f'Введите {N} {get_piece_form(N, 2)} {get_piece_form(N)} через пробел или запятую:\n')
        input_numbers = user_input.replace(',', ' ').split()
        for i in input_numbers:
            try:
                num = int(i)
                if not (-20e9 <= num <= 20e9):
                    print(f'Число {num} не входит в диапазон от -20e9 до 20e9. Введите строку заново.')
                    numbers.clear()
                    break
                numbers.add(num)
            except ValueError:
                print('Некорректный ввод числа. Введите строку заново.')
                numbers.clear()
                break
        if len(numbers) != N:
            print(f'Количество разных чисел в списке не равно {N}, введите строку заново')
            numbers.clear()
    except ValueError:
        print('Некорректный ввод строки чисел.')

print(f'Количество разных чисел в множестве равно {len(numbers)}')
input()
