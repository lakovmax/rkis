from collections import Counter

def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))

sequence = input("Введите строку из цифр от 0 до 9: ")
print(count_it(sequence))