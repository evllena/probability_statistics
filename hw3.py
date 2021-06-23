import numpy as np
from math import factorial as fl


def comb(k, n):
    return fl(n) / (fl(k) * fl(n - k))


# TASK1

salary = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

mean = salary.sum() / salary.size
st_deviation = (np.sum((salary - mean) ** 2) / salary.size) ** 0.5
bias_variance = np.sum((salary - mean) ** 2) / salary.size
unbias_variance = np.sum((salary - mean) ** 2) / (salary.size - 1)

print("1:")
print(f"Среднее арифметическое зарплат выпускников - {mean}")
print(f"Среднее квадратичное отклонение зарплат выпускников - {round(st_deviation, 2)}")
print(f"Смещенная дисперсия зарплат выпускников - {bias_variance}")
print(f"Несмещенная дисперсия зарплат выпускников - {round(unbias_variance, 2)}")

# TASK 2

print("2:")
P1 = (comb(0, 5) * comb(2, 3)) / comb(2, 8) * ((comb(3, 5) * comb(1, 7)) / comb(4, 12))
P2 = (comb(1, 5) * comb(1, 3)) / comb(2, 8) * ((comb(2, 5) * comb(2, 7)) / comb(4, 12))
P3 = (comb(2, 5) * comb(0, 3)) / comb(2, 8) * ((comb(1, 5) * comb(3, 7)) / comb(4, 12))
print(P1, P2, P3)
print(f"Вероятность того, что 3 мяча белые - {round(P1 + P2 + P3, 7)}")
