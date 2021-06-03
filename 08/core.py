import os
import shutil
import datetime
import random


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('already exist')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def chDir(name):
    os.chdir(name)
    print(os.getcwd())


def game():
    number = int(input('Please make a number (1-100): '))
    clue = None
    x = 1
    y = 100
    is_winner = False
    while not is_winner:
        computer_number = random.randint(x, y)
        print(f'Computer have chosen the number {computer_number} ')
        if computer_number == number:
            is_winner = True
            break
        else:
            clue = input(
                'Please give me a clue is my number more or less than yours?: ')
            if clue == "less":
                x = computer_number
            elif clue == "more":
                y = computer_number

    print('Computer wins!')
