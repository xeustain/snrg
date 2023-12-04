N = 0
while N <= 0 or N >= 100000:
    N = int(input("Число N:\n"))
Ai = []

for i in range(N):
    numbers = 0
    while numbers <= 0 or numbers >= 10e9:
        numbers = int(input(f"Введите число #{i+1}:\n"))
    Ai.append(numbers)
last_num = Ai.pop()
Ai.insert(0, last_num)
print(Ai)