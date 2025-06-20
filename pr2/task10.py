elements = []
while True:
    a = input(f'Введите элемент: ')
    if a == "":
        break
    elements.append(a)
if elements:
    short = min(elements, key=len)
    long = max(elements, key=len)

print(f'Самый короткий элемент: {short}')
print(f'Самый длинный элемент: {long}')