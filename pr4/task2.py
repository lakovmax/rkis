import random

def func():
    length = 15
    result = []
    number_a = random.randint(1, 100)

    for i in range(length-1):
        result.append(int(input("Enter a number: ")))

    s = sum(result)
    result.append(s)
    for i in result:
        print(i, end=" ")

func()