import math

def get_piece_form(num):
    if 11 <= num % 100 <= 14:
        return " лодок"
    elif num % 10 == 1:
        return " лодка"
    elif 2 <= num % 10 <= 4:
        return " лодки"
    else:
        return " лодок"
    
fishermen = 0
tonnage = 0
fishermen_mass = []

while tonnage <= 1 or tonnage >= 10e6:
    tonnage = int(input("Сколько может вместить в себя лодка? Введите вместимость, выраженную в массе (КГ):\n"))
    if tonnage > 10e6 or tonnage < 1:
        print(f"Грузоподъёмность не может быть равна: {tonnage}")

while fishermen <= 1 or fishermen >= 100:
    fishermen = int(input("Сколько рыбаков на берегу?:\n"))
    if fishermen > 100 or fishermen < 1:
        print(f"Количество рыбаков не может быть равно: {fishermen}")

for i in range(fishermen):
    fisherman_mass = 0
    while fisherman_mass <= 1 or fisherman_mass >= tonnage:
        fisherman_mass = int(input(f"Введите массу рыбака #{i + 1}\n"))
        if fisherman_mass > tonnage or fisherman_mass < 1:
            print("Некорректная масса рыбака")
    fishermen_mass.append(fisherman_mass)

total_mass = sum(fishermen_mass)
boats_number = math.ceil(total_mass / tonnage) 
# Мне больше нравится c библиотекой, я мог бы в следующей строке прибавить единицу к целому числу, если остаток от деления на 1 > 0 
print(f"Понадобится {boats_number}{get_piece_form(boats_number)}!")
input()