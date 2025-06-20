def func():
    a, b = int(input("Введите длину прямоугольника: ")), int(input("Введите ширину прямоугольника: "))
    c = int(input("Введите сторону квадрата: "))
    s = a * b
    q = c**2
    k = s / q
    print(k)
func()