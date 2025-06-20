import random

def func():
    length = 15
    result = []
    number_a = random.randint(1, 100)

    for i in range(length):
        result.append(number_a)
        number_a += random.randint(1, 5)

    for i in result:
        print(i, end=" ")

func()
