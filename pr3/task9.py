import random


def func(x, array):
    return x in array

x = random.randint(1, 30)
a = []
for i in range(random.randint(1, 30)):
    a.append(i)
print(f'a: {a}\nx: {x}\n{func(x, a)}')