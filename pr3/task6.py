def func():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = 1
    for i in a:
        if a.index(i) % 2:
            b *= i
    else:
        print(f'Произведение чисел которые стоят на нечётных местах: {b}')
func()