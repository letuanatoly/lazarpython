def minus(start, end, f):
    if start < end or start == end and not f:
        return 0
    
    if start == end and f:
        return 1
    
    if start == 25:
        f = True
    
    if start > end:
        return minus(start - 2, end, f) + minus(start - 3, end, f) + minus(start - 4, end, f)

i25 = False
print(minus(47, 14, i25))