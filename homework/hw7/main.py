def age_word(age: int) -> str:
    if 11 <= age % 100 <= 14:
        return "лет"
    if age % 10 == 1:
        return "год"
    if 2 <= age % 10 <= 4:
        return "года"
    return "лет"

with open('web_clients_correct.csv','r') as client_data:
    headers = client_data.readline().strip().split(',')

    class Clients:
        name_index = headers.index('name')
        device_index = headers.index('device_type')
        browser_index = headers.index('browser')
        sex_index = headers.index('sex')
        age_index = headers.index('age')
        bill_index = headers.index('bill')
        region_index = headers.index('region')

    with open('info.txt', 'w') as out:
        for data in client_data:
            value = data.strip().split(',')

            name = value[Clients.name_index]
            device = value[Clients.device_index]
            browser = value[Clients.browser_index]
            sex = value[Clients.sex_index]
            age = int(value[Clients.age_index])
            bill = value[Clients.bill_index]
            region = value[Clients.region_index]

            sex_text = "женского пола" if sex.lower() == "female" else "мужского пола"
            age_text = age_word(age)
            line = (
                f"Пользователь {name} {sex_text}, {age} {age_text} совершил(а) покупку "
                f"на {bill} у.е. с {device} браузера {browser}. "
                f"Регион, из которого совершалась покупка: {region}\n"
            )

            out.write(line)