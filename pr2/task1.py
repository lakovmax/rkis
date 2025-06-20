import random
a = []
number = 0
while number <= 10:
    number += 1
    a.append(random.randint(1,100))
print(a)
print(f'Минимальный элемент коллекции: {min(a)}')
