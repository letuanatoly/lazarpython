f = open(input("Введите имя файла: "))
data = []
for line in f:
    data.append([int(x) for x in line.split()])
f.close()
lots = sorted({d[0] for d in data})
sold = []
for lot in lots:
    stavki = []
    for d in data:
        if d[0] == lot:
            stavki.append(d[2])
    if len(stavki) >= 2:
        stavki.sort()
        sold.append([lot, stavki[-2]])

sum = 0
for s in sold:
    sum += s[1]
print(len(sold), sum)