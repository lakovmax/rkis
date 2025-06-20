def func():
    a = []
    b = [a.append(x) for x in input('Введиет элементы списка через пробел: ').split(' ')]
    print(a)
    print(f'Минимальный элемент массива: {min(a)}')
func()