import numpy as np
from math import factorial as fl


def comb(k, n):
    return fl(n) / (fl(k) * fl(n - k))


def bern_form(k, n, p):
    q = 1 - p
    return comb(k, n) * p ** k * q ** (n - k)


def pua_form(m, n, p):
    lambda_ = n * p
    return (lambda_ ** m / fl(m)) * np.exp(-lambda_)


print("1:")
print(f"Вероятность того, что стрелок попадет в цель ровно 85 раз - {round(bern_form(85, 100, 0.8), 7)}")

print("2:")
print(f"Вероятность ,что ни одна из лампочек не перегорит в первый день - {round(pua_form(0, 5000, 0.0004), 7)}")
print(f"Вероятность ,что перегорят две лампочки - {round(pua_form(2, 5000, 0.0004), 7)}")

print("3:")
print(f"Вероятность, что орел выпадет 70 раз - {round(bern_form(70, 144, 0.5), 7)}")

print("4:")
print(f"Вероятность, что все мячи белые - {round(comb(2, 7) / comb(2, 10) * comb(2, 9) / comb(2, 11), 7)}")
f1 = comb(2, 7) / comb(2, 10) * comb(2, 2) / comb(2, 11)
f2 = comb(2, 3) / comb(2, 10) * comb(2, 9) / comb(2, 11)
f3 = comb(1, 7) * comb(1, 3) / comb(2, 10) * comb(1, 9) * comb(1, 2) / comb(2, 11)
print(f"Вероятность, что ровно два мяча белые - {round(f1 + f2 + f3, 7)}")
print(
    f"Вероятность, что хотя бы один мяч белый - {round(1 - (comb(2, 3) / comb(2, 10) * comb(2, 2) / comb(2, 11)), 7)}")
