data = []

f = open(input("Введите имя файла: "))
next(f)  # Пропускаем заголовок (первая строка)
for line in f:
    data.append(line.strip().split('\t'))
# Проверка
for row in data:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")