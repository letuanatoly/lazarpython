f = open(input("Введите имя файла: "))
s = f.read()
f.close()

i = 0 # позиция в строке, начиная с первого символа
n = len(s)
isSeq = False
l = 0 # длина
ml = 0 # максимальная длина
while i < n:
    if i + 3 < n and s[i : i + 3] == "DOG":
        # найденый целый кусок на 3 символа
        i += 3
        if isSeq:
            l += 3
        else:
            isSeq = True
            l = 3
    elif i + 2 < n and s[i : i + 2] == "DO":
        i += 2
        if isSeq:
            l += 2
            isSeq = False
            # на коротких кусках обрывается последовательность
        else:
            l = 2
    elif s[i] == 'D':
        i += 1
        if isSeq:
            l += 1
            isSeq = False
        else:
            l = 1
    else:
        isSeq = False
        i += 1
    
    if not isSeq:
        if l > ml:
            ml = l
        l = 0
# если самая длинная последовательность упирается в край файла
if l > ml:
    ml = l

print(ml)