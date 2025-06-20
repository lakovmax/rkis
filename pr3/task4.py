def func():
    a, b = int(input("Введите число: ")), int(input("Введите ещё число: "))
    if  a > b:
        print(f'Наибольшее число: {a}')
    else:
        print(f'Наибольшее число: {b}')
func()