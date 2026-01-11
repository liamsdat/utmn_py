year = int(input('Enter year: '))
print("Високосный") if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else print("Не високосный")