import collections

pets = {}

def create():
    print("Создать карточку питомца")
    key = input("Кличка питомца:\n >>> ")
    fields = ["Вид питомца", "Возраст питомца", "Имя владельца"]
    temp = {key: dict()}
    for field in fields:
        res = input(f"{field}:\n>>> ")
        temp[key][field] = int(res) if res.isnumeric() else res

    if pets:
        last = max(pets.keys())
    else:
        last = 0

    pets[last + 1] = temp

def read():
    print("Чтение карточки питомца")
    ID = int(input("Введите ID:\n>>> "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
    key = next(iter(pet.keys()))
    string = (
        f'Это {pet[key]["Вид питомца"]} по кличке "{key}". '
        f'Возраст питомца: {pet[key]["Возраст питомца"]} {get_suffix(pet[key]["Возраст питомца"])}. '
        f'Имя владельца: {pet[key]["Имя владельца"]}'
    )
    print(string)


def update():
    print("Обновление данных")
    ID = int(input("Введите ID:\n>>> "))
    pet = get_pet(ID)
    if not pet:
        print(f"Невозможно обновить данные: питомца с ID:{ID} нет в базе.")
        return

    old_key = next(iter(pet.keys()))
    new_key = input("Введите старое или новое имя питомца:\n>>> ")
    if new_key and new_key != old_key:

        pets[ID][new_key] = pets[ID].pop(old_key)
        if not any(pets[ID][new_key].values()):
            del pets[ID][new_key]
            print("Невозможно обновить данные: новое имя питомца не может быть пустым.")
            return


    print("Введите данные или оставьте поле пустым. Нажмите Enter\n>>> ")
    temp = dict()
    for field, value in pets[ID][new_key].items():
        res = input(f"{field}: ")
        if res:
            temp[field] = int(res) if res.isnumeric() else res


    pets[ID][new_key].update(temp)

def delete():
    print("Удаление карточки питомца\n >>> ")
    ID = int(input("Введите ID:\n>>> "))
    pets.pop(ID, None)

def get_pet(ID):
    return pets.get(ID, False)

def pets_list():
    for key, val in pets.items():
        print(f"ID:{key}", val)

commands = {
    "Создать": create,
    "Открыть": read,
    "Обновить": update,
    "Удалить": delete,
    "Показать всё": pets_list,

    "Выход": 0,
}

def print_commands():
    print("Список доступных команд:")
    for key in commands:
        print("> ", key)


def get_suffix(age):
    if isinstance(age, int):
        if age % 10 == 1 and age != 11:
            return "год"
        elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
            return "года"
        else:
            return "лет"
    else:
        return "лет"
    
while True:
    print_commands()
    command = input("Введите команду:\n>>> ")
    if command not in commands.keys():
        continue
    if command == "Выход":
        exit()
    commands[command]()