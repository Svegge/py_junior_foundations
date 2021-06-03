"""
3. Напишите функцию которая принимает на вход список. Функция создает из этого
   списка новый список из квадратных корней чисел (если число положительное) и
   самих чисел (если число отрицательное) и возвращает результат (желательно
   применить генератор и тернарный оператор при необходимости). В результате
   работы функции исходный список не должен измениться. Например:

old_list = [1, -3, 4] result = [1, -3, 2]

    Примечание: Список с целыми числами создайте вручную в начале файла.
    Не забудьте включить туда отрицательные числа.
    10-20 чисел в списке вполне достаточно.
"""
from copy import deepcopy


def list_handling(user_list: list):
    func_list = deepcopy(user_list)
    result_list = [i**2 if i > 0 else i for i in func_list]
    return result_list


custom_list = [i for i in range(-10, 10)]

print('source list:', custom_list)

modified_list = list_handling(custom_list)

print('modified list:', modified_list)
