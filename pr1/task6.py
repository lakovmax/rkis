def season_events(number_of_month):
    number_of_month = int(input("Введите РЕАЛЬНЫЙ номер месяца вашего рождения: "))
    month = {1: "Январь",
             2: "Февраль",
             3: "Март",
             4: "Апрель",
             5: "Май",
             6: "Июнь",
             7: "Июль",
             8: "Август",
             9: "Сентябрь",
             10: "Октябрь",
             11: "Ноябрь",
             12: "Декабрь" }
    if number_of_month == 1 or number_of_month == 2 or number_of_month == 12:
        print(f'Вы родились в {month[number_of_month]}. За окном падал белый снег')
    if number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
        print(f'Вы родились в {month[number_of_month]}. Птицы пели прекрасные песни')
    if number_of_month == 6 or number_of_month == 7 or number_of_month == 8:
        print(f'Вы родились в {month[number_of_month]}. Солнце светило ярче чем когда-либо')
    if number_of_month == 9 or number_of_month == 10 or number_of_month == 11:
        print(f'Вы родились в {month[number_of_month]}. Урожай был невероятным')

season_events(1)