import numpy as np

# TASK1


std = 16
y = 0.95
mean_sample = 80
n = 256
z = 1.96
s = std / n ** 0.5
print("1:")
print(f"Доверительный интервал: {mean_sample - z * s} - {mean_sample + z * s}")

# TASK2

data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
n1 = 10
y1 = 0.95
z1 = 1.96
mean_sample1 = np.mean(data)
std1 = np.std(data)
s1 = std1 / n1 ** 0.5
print("2:")
print(f"Доверительный интервал: {round(mean_sample1 - z1 * s1, 3)} - {round(mean_sample1 + z1 * s1, 3)}")

# TASK3

std2 = 2
y2 = 0.95
mean_sample2 = 17.5
n2 = 100
z2 = 1.96
s2 = std2 / n2 ** 0.5
print("3:")
print(f"Доверительный интервал: {mean_sample2 - z2 * s2} - {mean_sample2 + z2 * s2} ")
print("Значение 17 не попадает в интервал. Гипотеза неверна")

# TASK4

data3 = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
n3 = 10
y3 = 0.99
z3 = 2.557
mean_sample3 = np.mean(data3)
std3 = np.std(data3)
s3 = std3 / n3 ** 0.5
print("4:")
print(f"Доверительный интервал: {round(mean_sample3 - z3 * s3, 3)} - {round(mean_sample3 + z3 * s3, 3)}")
print("Значение 200 попадает в интервал. Гипотеза верна")