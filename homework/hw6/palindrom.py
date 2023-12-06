word = input("Введите слово:\n>>>")

reversed_word = word[::-1]

if word == reversed_word:
    print(f"Да, слово {word} является палиндромом")
else:
    print(f"Нет, слово {word} не является палиндромом")

input()