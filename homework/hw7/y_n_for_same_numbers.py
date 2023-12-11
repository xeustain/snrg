numbers_set = set()
input_sequence = input("Введите последовательность чисел через пробел:\n")
numbers_list = list(map(int, input_sequence.split()))

for number in numbers_list:
    if number in numbers_set:
        print("YES")
    else:
        print("NO")
        numbers_set.add(number)

input()