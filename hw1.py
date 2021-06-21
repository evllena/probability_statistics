import math


def comb(k, n):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


# all results were rounded to 7 decimals


print("1a:")
print(f"Вероятность того, что все карты – крести - {round(comb(4, 13) / comb(4, 52), 7)}")

print("1b:")
print(
    f"Вероятность, что среди 4 карт окажется хотя бы один туз - {round(1 - comb(0, 4) * comb(4, 48) / comb(4, 52), 7)}")

print("2:")
print(f"Вероятность того, что человек, не знающий код, откроет дверь с первой попытки - {round(1 / comb(3, 10), 7)}")

print("3:")
print(f"Вероятность того, что все извлеченные детали окрашены - {round(comb(3, 9) / comb(3, 15), 7)}")

print("4:")
print(f"Вероятность того, что 2 приобретенных билета окажутся выигрышными - {round(comb(2, 2) / comb(2, 100), 7)}")
