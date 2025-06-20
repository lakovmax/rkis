def func(numbers):
    numbers = str(numbers)
    for i in range(len(numbers) - 1):
        if int(numbers[i]) <= int(numbers[i + 1]):
            return False
    return True

numbers = input("Введите число: ")
print(func(numbers))