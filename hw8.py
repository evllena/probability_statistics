import numpy as np


y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182], dtype=np.float64)
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180], dtype=np.float64)
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170], dtype=np.float64)

n1 = len(y1)
n2 = len(y2)
n3 = len(y3)
n = n1 + n2 + n3

k = 3

y1_mean = np.mean(y1)
print(f'Средний рост футболистов - {y1_mean}')

y2_mean = np.mean(y2)
print(f'Средний рост хоккеистов - {y2_mean}')

y3_mean = np.mean(y3)
print(f'Средний рост штангистов - {y3_mean}')

y_all = np.concatenate([y1, y2, y3])

y_mean = np.mean(y_all)
print(f'Средний рост - {y_mean}')

s2 = np.sum((y_all - y_mean)**2)
print(f'Сумма квадратов отклонений наблюдений от общего среднего - {s2}')

s2_f = ((y1_mean - y_mean)**2) * n1 + ((y2_mean - y_mean)**2) * n2 + ((y3_mean - y_mean)**2) * n3
print(f'Сумма квадратов отклонений средних групповых значений от общего среднего - {s2_f}')

s2_residual = s2 - s2_f
print(f'Остаточная сумма квадратов отклонений - {s2_residual}')

sigma2_general = s2 / (n - 1)
print(f'Общая дисперсия - {sigma2_general}')

sigma2_f = s2_f / (k - 1)
print(f'Факторная дисперсия - {sigma2_f}')

sigma2_residual = s2_residual / (n - k)
print(f'Остаточная дисперсия - {sigma2_residual}')

F_h = sigma2_f / sigma2_residual
print('F_h -', F_h)

F_k = 3.385

eta2 = s2_f / s2
print(eta2)
