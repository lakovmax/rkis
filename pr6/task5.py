A = ["abc", "caac", "CbaC", "x", "cc", "c", "CQC", "123C"]
C = input("Введите C: ")
count = 0

for s in A:
    if len(s) > 1 and s.startswith(C) and s.endswith(C):
        count += 1

print(f"Строка: {A}")
print(f"Количество подходящих элементов: {count}")