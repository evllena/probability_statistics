import math

# TASK1

def aver_value(a, b):
    return (a + b) / 2


def disp(a, b):
    return (b - a) ** 2 / 12


print("1:")
print(f"Среднее значение величины- {aver_value(200, 800)}")
print(f"Дисперсия величины - {disp(200, 800)}")


# TASK2

D = 0.2
a = 0.5

# b**2 - b + 0.25 = 2.4

disc = ((-1) ** 2) - 4 * 1 * (-2.15)

x1 = (1 + math.sqrt(disc)) / (2 * 1)
x2 = (1 - math.sqrt(disc)) / (2 * 1)
print('2:')
print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
print(f'Правая граница распределения b = {x1}')
print(f'Среднее значение - {aver_value(0.5, x1)}')
