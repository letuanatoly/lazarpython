# читаем файл
f = open("D:\\1\\processes.txt", encoding="utf-8")
lines = f.readlines()
f.close()

ids = []
times = []
deps = []

# разбираем строки
for line in lines[1:]:
    p = line.strip().split("\t")
    ids.append(int(p[0]))
    times.append(int(p[1]))
    if p[2] == "0":
        deps.append([])
    else:
        deps.append([int(x) for x in p[2].split(";")])

n = len(ids)

start = [0] * n
finish = [0] * n

print(start)
print(finish)

# считаем ранние старты
for i in range(n):
    if deps[i] == []:
        start[i] = 1
    else:
        max_end = 0
        for d in deps[i]:
            j = ids.index(d)
            if finish[j] > max_end:
                max_end = finish[j]
        start[i] = max_end + 1

    finish[i] = start[i] + times[i] - 1

# считаем процессы на 12-й мс
t = 12
count = 0
for i in range(n):
    if start[i] <= t <= finish[i]:
        count += 1

print(count)
