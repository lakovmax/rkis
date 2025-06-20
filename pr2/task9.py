def func():
    a = int(input("Введите число: "))
    b = int(input("Введите ещё число: "))
    if a > b:
        print(f'{a} больше {b}')
    elif b > a:
        print(f'{b} больше {a}')
    else:
        print(f'Числа равны')
func()