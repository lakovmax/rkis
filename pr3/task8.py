import random

def func():
    length = random.randint(1, 25)
    result = []
    number_a = random.randint(3, 300)
    for i in range(length):
        if number_a % 3 == 0:
            result.append(number_a)
            number_a -= 3
        else:
            number_a -= number_a % 3
        if number_a == 0:
            break
    return result

print(func())