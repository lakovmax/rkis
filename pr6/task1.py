names = ["Иван", "Пётр", "Антон", "Олег", "Михаил", "Кирилл", "Артём", "Дмитрий", "Вадим", "Александр"]
print(f"Имена: {names}")
for name in names:
    if name.lower().startswith('а'):
        print(name)