def solve():
    for s in range(1, 52):
        # Петя может сделать +1
        if s + 1 >= 52:
            return s
        # Петя может сделать *2
        if s * 2 >= 52:
            return s

result = solve()
print(f"Минимальное S, при котором Петя выигрывает первым ходом: {result}")