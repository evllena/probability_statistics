import numpy as np


# TASK1

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov1 = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
cov2 = np.cov(zp, ks, ddof=0)[0, 1]
cor1 = cov1 / (np.std(zp) * np.std(ks))
cor2 = np.corrcoef(zp, ks)[0, 1]
print('1:')
print(f"Найденные ковариации - {cov1}, {cov2}")
print(f"Найденные коэффициенты корреляции - {cor1}, {cor2}")


# TASK2

data2 = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
n2 = 10
y2 = 0.95
z2 = 1.96
mean_sample2 = np.mean(data2)
std2 = np.std(data2)
s2 = std2 / n2 ** 0.5

print("2:")
print(f"Доверительный интервал: {round(mean_sample2 - z2 * s2, 3)} - {round(mean_sample2 + z2 * s2, 3)}")


# TASK3

n3 = 27
y3 = 0.95
z3 = 1.96
mean_sample3 = 174.2
std3 = 5
s3 = std3 / n3 ** 0.5
print("3:")
print(f"Доверительный интервал: {round(mean_sample3 - z3 * s3, 3)} - {round(mean_sample3 + z3 * s3, 3)}")
