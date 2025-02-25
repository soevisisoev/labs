def find_min_n():
    n = 2
    while True:
        for a in range(1, int(n ** (1 / 3)) + 1):
            for b in range(a, int(n ** (1 / 3)) + 1):
                if a ** 3 + b ** 3 == n:
                    return n
        n += 1
result = find_min_n()
print("Крутое число:", result)
