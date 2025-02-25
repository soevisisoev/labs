import math

a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
h = float(input("Введите шаг h: "))

print("x\t\tF(x)")
x = a
while x <= b:
    F_x = x - math.sin(x)
    print(f"{x:.4f}\t{F_x:.4f}")
    x += h