"""
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и
group.pickle, прочитать из них информацию. И получить объект: словарь из
предыдущего задания.
"""

import json
import pickle

with open('group.json', encoding='utf-8') as file:
    json_data = json.load(file)

print(json_data)

with open('group.pickle', 'rb') as file:
    pickle_data = pickle.load(file)

print(pickle_data)
