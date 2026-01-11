# Перечень всех документов
documents = [
    {'type' : 'passport', 'number':'2207 876234', 'name': 'Василий Гупкин'},
    {'type' : 'invoice', 'number':'11-2', 'name': 'Геннадий Покемонов'},
    {'type' : 'insurance', 'number':'10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876324', '11-2'],
    '2': ['10006'],
    '3': []
}
            
def find_doc_owner():
    user_input = str(input('Введите номер документа, чтобы узнать его владельца --> '))
    found = False
    for doc in documents:
        if doc['number'] == user_input:
            found = True
            break
    
    if found:
        print(f"Владелец документа: {doc['name']}")
    elif user_input in ('q', 'quit'):
        return
    else:
        print('Документа нет в базе')
        find_doc_owner()

def find_directory_doc():
    user_input = str(input('Введите номер документа, чтобы узнать его полку --> '))
    found = False
    for dir, doc in directories.items():
        if user_input in doc:
            found = True
            break
    
    if found:
        print(f"Документ на полке: №{dir}")
    elif user_input in ('q', 'quit'):
        return
    else:
        print('Документа нет на полке')
        find_directory_doc()

def cli():
    while True:
        command = str(input('Введите команду --> '))
        if command == 'p':
            find_doc_owner()
        elif command == 's':
            find_directory_doc()
        elif command in ('q', 'quit'):
            break
        else:
            print('Неизвестная команда')


cli()