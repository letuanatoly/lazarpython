data = []

f = open(input("Введите имя файла: "))
next(f)  # Пропускаем заголовок (первая строка)
for line in f:
    data.append(line.strip().split('\t'))

# добавление процессов в каждый момент времени (в мс)
tp = [] # каждая строка с одномерным массивом idB в данный момент от 0 до 99
for t in range(100):
    tp.append([]) # подготовили 100 строк для каждой милисекунды времени

for t in range(100):
    for row in data:
        idB = int(row[0])
        isMissing = True # процесса нет ещё в таблице
        for tB in range(t): # проверка во все моменты времени до текущего
            if idB in tp[tB]: # каждая строка tp это массив с idB процессов
                # это процесс уже занесён в tp
                isMissing = False
                break
        if isMissing: # id ещё нет в списке процессов
            deps = row[2].split(';') # список зависимостей
            isDepsRan = True # зависимости отработали
            if deps != ['0']:
                for idAs in deps: # проверяем, что все зависимости отработали
                    idA = int(idAs)
                    isAstarted = False # Процесс A был запущен до времени t
                    for tA in range(t):
                        if idA in tp[tA]:
                            isAstarted = True
                            break
                    if not isAstarted or idA in tp[t]:
                        # Был не запущен или ещё не завершён
                        isDepsRan = False
                        break
            if isDepsRan:
                for tB in range(t, t + int(row[1])): # с этого момента и далее
                    #добавляем idB в каждый следующий момент до истечение срока
                    tp[tB].append(idB)
for t in range(100):
    if tp[t] != []:
        print(f"{t}\t{tp[t]}")  