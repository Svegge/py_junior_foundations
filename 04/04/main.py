"""
4: Давайте усложним предыдущее задание. Измените сущности, добавив новый
параметр - armor = 1.2 (величина брони персонажа) Теперь надо добавить новую
функцию, которая будет вычислять и возвращать полученный урон по формуле damage
/ armor Следовательно, у вас должно быть 2 функции:

    Наносит урон. Это улучшенная версия функции из задачи 3.

    Вычисляет урон по отношению к броне.

    Примечание. Функция номер 2 используется внутри функции
    номер 1 для вычисления урона и вычитания его из здоровья персонажа.
"""

user_name = input('Введите имя ')

player = {
    'name': user_name,
    'health': 100,
    'damage': 50,
    'armour': 1.2,
}

enemy = {
    'name': 'enemy',
    'health': 100,
    'damage': 50,
    'armour': 1.2,
}


def get_adjusted_damage(damage, defender):
    adjusted_damage = damage / defender['armour']
    return adjusted_damage


def attack(attacker, defender):
    damage = attacker['damage']
    adjusted_damage = get_adjusted_damage(damage, defender)
    defender['health'] -= adjusted_damage


attack(player, enemy)

print(enemy['health'])

attack(player, enemy)

print(enemy['health'])
