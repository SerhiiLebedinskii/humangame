
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
    if work:
        print('Отработал я, чем займусь')
    else:
        print('Чем займусь')
    event = input('Введите занятие')
    if unit_time > 48:
        break


