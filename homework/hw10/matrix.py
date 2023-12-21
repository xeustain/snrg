import random
import time

height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))

matrix_1 = [[random.randint(-999, 999) for j in range(width)] for i in range(height)]
print('Первая матрица:')
for i in range(height):
    print(matrix_1[i])

matrix_2 = [[random.randint(-999, 999) for j in range(width)] for i in range(height)]
print('Вторая матрица:')
for i in range(height):
    print(matrix_2[i])

result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(width)] for i in range(height)]
print("Результат сложения двух матриц:")
for i in range(height):
    print(result[i])

time.sleep(5)
