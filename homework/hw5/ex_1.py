from datetime import datetime

journals = [
    ("The Moscow Times", "Wednesday, October 2, 2002"),
    ("The Guardian", "Friday, 11.10.13"),
    ("Daily News", "Thursday, 18 August 1977")
]

FORMATS = [
    "%A, %B %d, %Y",
    "%A, %d.%m.%y",
    "%A, %d %B %Y"
]

def parse_date(date_str, formats):
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать дату: {date_str}")

for journal, date_str in journals:
    try:
        parsed = parse_date(date_str, FORMATS)
        print(f"{journal} : {parsed}")
    except ValueError as e:
        print(f"{journal}: ошибка {e}")
