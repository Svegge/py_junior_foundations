"""
1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей
любимой музыкальной группы, например:

my_favourite_group = {'name': 'Г.М.О.','tracks': ['Последний месяц осени',
'Шапито'],'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name':
'Шапито','year': 2014}]} С помощью модулей json и pickle сериализовать данный
словарь в json и в байты, вывести результаты в терминал. Записать результаты в
файлы group.json, group.pickle соответственно. В файле group.json указать
кодировку utf-8.
"""
import json
import pickle

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок',
         'year': 2016},
        {'name': 'Шапито',
         'year': 2014}
    ]
}
serialized_data_json = json.dumps(my_favourite_group)
serialized_data_pkl = pickle.dumps(my_favourite_group)

print(serialized_data_json)
print(serialized_data_pkl)

with open('group.json', 'w', encoding='utf-8') as file:
    json.dump(my_favourite_group, file)

with open('group.pickle', 'wb') as file:
    pickle.dump(my_favourite_group, file)

print('end')
