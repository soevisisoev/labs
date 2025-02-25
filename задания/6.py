def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
decimal_number = int(input("Введите натуральное число: "))
binary_number = decimal_to_binary(decimal_number)
print(f"Двоичное представление числа {decimal_number}: {binary_number}")