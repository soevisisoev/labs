epsilon = float(input("Введите значение epsilon: "))

a_prev = 1.0
n = 1
while True:
    a_n = 0.5 * (a_prev + 2 / a_prev)
    if abs(a_n**2 - 2) < epsilon:
        break
    a_prev = a_n
    n += 1

print(f"Наименьший номер n: {n}")
print(f"Элемент a_n: {a_n}")