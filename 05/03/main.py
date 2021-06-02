"""
3: Создайте модуль main.py.
 Из модулей реализованных в заданиях 1 и 2
  сделайте импорт в main.py всех функций.
   Вызовите каждую функцию в main.py и
   проверьте что все работает как надо.

Примечание: Попробуйте импортировать как весь
 модуль целиком (например из задачи 1),
 так и отдельные функции из модуля.

"""

import functions_one
from functions_two import get_random_list_item

functions_one.create_dirs()
functions_one.remove_dirs()

my_list = [1, 2, 6, 7, 8, 9, 34, 234]

random_item = get_random_list_item(my_list)

print(random_item)
