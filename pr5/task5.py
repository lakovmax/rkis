def func(a,b):
    return ( a + 4 * b ) * ( a - 3 * b ) + a * 2

a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(f'Результат: {func(a,b)}')