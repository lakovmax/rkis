from datetime import datetime
a = input("Введите имя: ")
now = datetime.now()
print(f'День недели: {now.strftime("%A")}')
print(f'Месяц: {now.strftime("%B")}')
print(f'Имя: {a}')