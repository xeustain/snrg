
def get_pet_info():
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    return {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name

    }

def print_age_phrase(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
        return "года"
    else:
        return "лет"

def main():
    pets = {}
    pet_count = int(input("Сколько питомцев вы хотите добавить в словарь? "))
    for i in range(pet_count):
        pet_name = input(f"Введите имя питомца #{i + 1}: ")
        pet_info = get_pet_info()
        pets[pet_name] = pet_info


    for pet_name, pet_info in pets.items():
        age_phrase = print_age_phrase(pet_info["Возраст питомца"])
        print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name.capitalize()}". Возраст питомца: {pet_info["Возраст питомца"]} {age_phrase}. Имя владельца: {pet_info["Имя владельца"].capitalize()}')

    chosen_pet = input("Введите имя питомца, о котором хотите получить информацию: ")
    chosen_pet = chosen_pet.lower()
    if chosen_pet in pets:
        pet_info = pets[chosen_pet]
        age_phrase = print_age_phrase(pet_info["Возраст питомца"])
        print(f'Выбранный питомец: {pet_info["Вид питомца"]} по кличке "{chosen_pet.capitalize()}". Возраст питомца: {pet_info["Возраст питомца"]} {age_phrase}. Имя владельца: {pet_info["Имя владельца"].capitalize()}')
    else:
        print("Питомец с указанным именем не найден.")

main()
