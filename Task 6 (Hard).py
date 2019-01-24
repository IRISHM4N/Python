person = {'name': '-', 'surname': '-', 'age': '-', 'weight': '-'}

person['name'] = input('Имя:')
person['surname'] = input('Фамилия:')
person['age'] = int(input('Возраст:'))
person['weight'] = int(input('Вес:'))

if person['age'] <= 40:
    if (person['weight'] >= 50) and (person['weight'] <= 120):
        print('Пациент в хорошем состоянии.')
    else:
        print('Пациент должен начать правильный образ жизни!')

else:
    if (person['weight'] >= 50) and (person['weight'] <= 120):
        print('Пациент в хорошем состоянии.')
    else:
        print('Пациенту требуется осмотр врача!')



