print("Добро пожаловать в программу, которая может выделять делать фонетический разбор слова, отделяя гласные от согласных")
word = input("Введите слово: ")
vowels = {"a", "e", "i", "o", "u"}
vowels_count = 0
consonants_count = 0
for letter in word:
    if letter in vowels:
        vowels_count += 1
    elif letter.isalpha():
        consonants_count += 1
if vowels_count == 0 or consonants_count == 0:
    print(False)
else:
    print("Количество гласных:", vowels_count)
    print("Количество согласных:", consonants_count)
