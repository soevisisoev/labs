
x1, y1 = 1, 1
x2, y2 = 2, 2
x3, y3 = 3, 3
area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
if area == 0:
    print(False)
else:
    print(True)