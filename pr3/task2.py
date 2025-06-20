a, b, c = (int(input("Введите 1-ое число: ")),
           int(input("Введите 2-ое число: ")),
           int(input("Введите 3-е число: ")))
a *= 2
b -= 3
c = c**2
s = a + b + c
print(f'{a} + {b} + {c} = {s}')
