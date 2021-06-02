"""
2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из
них.
"""


def get_max_number(*args):
    num_list = []
    for i in args:
        num_list.append(float(i))
    max_number = max(num_list)
    return max_number


my_max_number = get_max_number(1, 20, 3, 4, 5)

print(my_max_number)
