"""
3: Давайте опишем пару сущностей player и enemy через словарь, который будет
иметь ключи и значения:

    name - строка полученная от пользователя,
    health = 100,
    damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
    ### Теперь надо создать функцию attack(person1, person2).
    # Примечание: имена аргументов можете указать свои.
    # ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
    # ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
    # Функция должна сама работать со словарями и изменять их значения.

"""

user_name = input('Введите имя ')

player = {
    'name': user_name,
    'health': 100,
    'damage': 50,
}

enemy = {
    'name': 'enemy',
    'health': 100,
    'damage': 50,
}


def attack(attacker, defender):
    defender['health'] -= attacker['damage']


attack(player, enemy)

print(enemy['health'])

attack(player, enemy)

print(enemy['health'])