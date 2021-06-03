"""
1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих
исходных списках.

    Примечание: Списки фруктов создайте вручную в начале файла.

"""

list_one = [
    'apple',
    'apricot',
    'banana',
    'blackberry',
    'blueberry',
    'cherry',
    'clementine',
]

list_two = [
    'fig',
    'gooseberry',
    'grape',
    'banana',
    'apple',
    'grapefruit',
    'kiwi',
]

list_three = [i for i in list_one if i in list_two]

print(list_three)
