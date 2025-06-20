def func():
    a = int(input(f'Напиши первое число: '))
    b = int(input(f'Напиши второе число: '))
    if b % a == 0:
        print(f'True')
    else:
        print(f'False')
func()