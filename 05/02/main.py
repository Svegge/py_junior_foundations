"""
2: Создайте модуль. В нем создайте функцию, которая принимает список
 и возвращает из него случайный элемент.
 Если список пустой функция должна вернуть None.
 Проверьте работу функций в этом же модуле.

    Примечание: Список для проверки введите вручную.
     Или возьмите этот: [1, 2, 3, 4]

"""

import random


def get_random_list_item(some_list):
    if len(some_list) == 0:
        result = None
    else:
        result = random.choice(some_list)
    return result


if __name__ == '__main__':

    custom_list = [1, 2, 3, 4]
    # custom_list = []
    random_item = get_random_list_item(custom_list)

    print(random_item)
