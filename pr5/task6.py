def invert_array(arr):
    inverted_arr = [-x for x in arr]
    return inverted_arr

def get_array_from_input():
        input_str = input("Введите числа через пробел: ")
        arr = [int(x) for x in input_str.split()]
        return arr

numbers = get_array_from_input()

inverted_numbers = invert_array(numbers)
print("Исходный массив:", numbers)
print("Инвертированный массив:", inverted_numbers)
