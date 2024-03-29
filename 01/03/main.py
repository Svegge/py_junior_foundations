"""
3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя
следующие данные: имя, фамилия, возраст и вес. Выведите результат согласно
которому:

    Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
    Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
    Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

    Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
    (Формула не соответствует реальной действительности и здесь используется только ради примера)

    Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.
    Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно.
    В случае ошибок, уточните условия для той или иной ситуации.

Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние Пример: Вася Пупкин, 31
год, вес 121 - следует заняться собой Пример: Вася Пупкин, 31 год, вес 49 -
следует заняться собой Пример: Вася Пупкин, 41 год, вес 121 - следует обратится
к врачу! Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
"""

input_data = input('Введите имя, фамилия, возраст и вес через пробел: ')
name, surname, age, weight = input_data.split()
age = int(age)
weight = float(weight)

if age <= 30 and 50 <= weight <= 120:
    condition = 'Пациент в хорошем состоянии'
elif age > 30 and weight < 50 or weight > 120:
    condition = 'Пациенту требуется заняться собой'
elif age > 40 and weight < 50 or weight > 120:
    condition = 'Пациенту требуется врачебный осмотр'


print(f'{name} {surname}, возраст - {age}, вес - {weight}: {condition}')
