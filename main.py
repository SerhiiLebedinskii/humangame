# import

human = {
    'name': 'John',
    'age': 25,
    'gender': 'male',
    'balance': 1000,
    'mood': 5,
    'time_balance': 300
}

work = True

unit_time = 0

while True:
    # читаем состояние персонажа
    if work:
        print('Отработал я, чем займусь')
    else:
        print('Чем займусь')
    event = input('Введите занятие')
    # обновляем состояние персонажа
    unit_time += 1
    if unit_time < 48:
        break


