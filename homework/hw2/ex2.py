boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
b, g = sorted(boys), sorted(girls)
if len(boys) != len(girls):
    print('Результат: Внимание, кто-то может остаться без пары.')
else:
    print('Идеальные пары')
    for k, v in dict(zip(b, g)).items():
        print(f'{k} и {v}')
    