data = {} # словарь для данных из файла

f = open(input("Введите имя файла: "))
next(f)  # Пропускаем заголовок (первая строка)
for line in f:
    # Разрезаем строку на 3 части по табуляции
    columns = line.strip().split('\t')
    idB = columns[0]
    duration = int(columns[1])
    idA = columns[2].split(';')
    # Добавляем в словарь
    data[idB] = [duration, idA]

# Проверка
for row in data:
    print(f"{row}\t{data[row][0]}\t{data[row][1]}")