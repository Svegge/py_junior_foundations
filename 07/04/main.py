"""
4. Написать функцию которая принимает на вход число от 1 до 100. Если число
   равно 13, функция поднимает исключительную ситуации ValueError иначе
   возвращает введенное число, возведенное в квадрат. Далее написать основной
   код программы. Пользователь вводит число. Введенное число передаем параметром
   в написанную функцию и печатаем результат, который вернула функция.
   Обработать возможность возникновения исключительной ситуации, которая
   поднимается внутри функции.
"""


def check_unlucky_number(user_number: int):
    try:
        if user_number == 13:
            raise ValueError('UnluckyNumber')
        elif user_number in range(0, 101):
            result_number = user_number ** 2
        else:
            print(
                'Your number is incorrect, enter something in range [0, 100]')
            result_number = None
    except ValueError:
        print('Your number is unlucky, try again')
        result_number = None

    return result_number


modified_number = check_unlucky_number(100)

print(modified_number)
