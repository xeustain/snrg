def factorial(n):
    if n == 0:
        return 1

    b = 1

    for i in range(1, n + 1):
        b *= i

    return b

def factorial_list(n):
    if n < 0:
        return "Ошибка: введите натуральное число"
    result = []
    value = 1
    for i in range(1, n + 1):
        value *= i
        result.append(value)
    return result


input_number = int(input('Введите натуральное число, факториал которого вы хотите найти: '))
result_list = factorial_list(input_number)
print(f'Факториал {input_number} равен {factorial(input_number)}')
result_list.reverse()
print(result_list)
input()
