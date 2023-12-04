import time

def function_1():
    num_cnt
    array = []
    for i in range(num_cnt):
        num = int(input(f"Введите число №{i + 1}\n\t>>>"))
        if abs(num) >= 1 and abs(num) <= 1e5:
            array.append(num)
        else:
            print("Вводите числа, 5которые не будут меньше единицы и больше ста тысяч по модулю!")
            i -= 1
    return array

def function_2(array):
    array.reverse()
    for num in array:
        if num < 0:
            num *= -1
        print(num)

def function_3():
    repeat_1 = input("Введите 'Y', чтобы начать заново или нажмите Enter, чтобы завершить\n")
    if repeat_1 == "":
        print("Выход...")
        time.sleep(1.5)
        exit()
    elif repeat_1 == "Y":
        num_cnt = 0
        function_4()
        
def function_4():
    num_cnt = 0
    while num_cnt <= 0 or num_cnt >= 10000:
        num_cnt = int(input("Введите количество чисел в массиве\n\t>>>"))
    if num_cnt <= 0 or num_cnt > 10000:
        print("Число должно быть больше нуля и меньше или равно десяти тысячам!")
        function_4()
    array = function_1()
    function_2(array)
    function_3()
num_cnt = 0
while num_cnt <= 0 or num_cnt >= 10000:
    num_cnt = int(input("Введите количество чисел в массиве\n\t>>>"))
    if num_cnt <= 0 or num_cnt > 10000:
        print("Число должно быть больше нуля и меньше или равно десяти тысячам!")
        function_4()
array = function_1()
function_2(array)
function_3()
input()