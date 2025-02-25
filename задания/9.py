def count_multiples(L, N, M):
    count = 0
    for number in range(L, N + 1):
        if number % M == 0:
            count += 1
    return count
L = int(input("Введите начало интервала (L): "))
N = int(input("Введите конец интервала (N): "))
M = int(input("Введите число M: "))
result = count_multiples(L, N, M)
print(f"Количество чисел, кратных {M} в интервале от {L} до {N}: {result}")