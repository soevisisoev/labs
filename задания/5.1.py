
N = int(input("Введите натуральное число N: "))
sum_N = sum(int(digit) for digit in str(N))
result_numbers = []
for num in range(1, N):
    product = 1
    for digit in str(num):
        product *= int(digit)
    if product == sum_N:
        result_numbers.append(num)
if result_numbers:
    print("Числа, удовлетворяющие условию:", result_numbers)
else:
    print("нет")