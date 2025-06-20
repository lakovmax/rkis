string = input("Введите строку: ")
if string.startswith("abc"):
    string = "www" + string[3:]
else:
    string += "zzz"
print(f"Новая строка: {string}")