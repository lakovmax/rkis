a = int(input(f'Введите число: '))
b = 0

if a > 1:
    for i in range(1, a + 1):
        b += i
elif a < 1:
    for i in range(a, 2):
        b += i
elif a == 1:
    print(2)
else:
    print(1)

print(f'Сумма: {b}')