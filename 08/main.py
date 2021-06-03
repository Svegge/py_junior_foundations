import sys
import random
from core import create_folder, create_file, get_list, delete_file, copy_file, save_info, chDir, game

save_info('Start')
try:
    command = sys.argv[1]
except IndexError:
    print('Please enter the command, for help enter help')
else:

    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('File name is missing')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Please enter the folder name, folder name is missing')
        else:
            create_folder(name)
    elif command == 'delete_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Object is missing, please enter the object name')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Please enter the names of objects')
        else:
            copy_file(name, new_name)

    elif command == 'chDir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Please enter the folder name')
        else:
            chDir(name)
    elif command == 'game':
        game()

    elif command == 'help':
        print('Список команд файлового менеджера:')
        print('1. list - получение информациии о вложенных папках и файлах')
        print('2. create_file - создание файла')
        print('3. create_folder - создание папки')
        print('4. delete_file - удаление файла или папки')
        print('5. copy - копирование файла или папки')
        print('6. help - вывод информации о доступных командах')
        print('7. chDir - смена рабочей директории')
        print(('8. game - игра угадай число'))

    save_info('End')
