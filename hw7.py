import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]).reshape(-1, 1)
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
model = LinearRegression().fit(zp, ks)
rr = model.score(zp, ks)
print(f'determination coefficient - {rr}')
intrcpt = model.intercept_
print(f'intercept (b0) - {intrcpt}')
coeff = model.coef_
print(f'slope (b1) - {coeff[0]}')

x_new = np.arange(200).reshape(-1, 1)
y_pred = model.predict(zp)
y_new = model.predict(x_new)


plt.plot(zp, ks, 'ro')
plt.grid(True)
plt.plot(x_new, y_new)
plt.plot(zp, y_pred)
plt.xlabel('Заработная плата')
plt.ylabel('Кредитный скоринг')
plt.show()