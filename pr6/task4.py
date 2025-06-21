arr = [-2, 0, -4, -1, 2, 4, 3, -8, 2, 0]
print(f"Числа: {arr}")
for num in arr:
    if num > 0:
        print(f"Первое положительное число: {num}")
        break
for num in reversed(arr):
    if num < 0:
        print(f"Последнее отрицательное число: {num}")
        break