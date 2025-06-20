def divide(x, y):
    try:
        result = x / y
        print("Результат:", result)
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    except TypeError:
        print("Ошибка: Неправильный тип данных")

divide(27, 13)
divide(45, 0)
divide(26, "2")
