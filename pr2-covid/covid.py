# 2020 Luis Espino
# 2021 Modified Javier Chin

from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read covid csv db
df = pd.read_csv('covid.csv')
columnas = df.columns.tolist()
fechas = []
contador = 1
totalesDias = []
totalesPorDia = []

for columna in columnas:
    if(columna[0] >= '0' and columna[0] <= '9'):
        fechas.append(columna)

for fecha in fechas:
    totalesPorDia.append(df[fecha].sum())
    totalesDias.append(contador)
    contador = contador + 1

# axis with real data
x = np.asarray(totalesDias)[:,np.newaxis]
y = np.asarray(totalesPorDia)[:,np.newaxis]
plt.scatter(x,y)

# Regresion grado 3
poly_degree = 4
polynomial_features = PolynomialFeatures(degree = poly_degree)
x_transform = polynomial_features.fit_transform(x)

model = LinearRegression().fit(x_transform, y)
y_new = model.predict(x_transform)

meanSquaredError = np.sqrt(mean_squared_error(y, y_new))
r2 = r2_score(y, y_new)
print('RMSE: ', meanSquaredError)
print('R2: ', r2)

# prediction
x_new_min = 0.0
x_new_max = 800.0

x_new = np.linspace(x_new_min, x_new_max, 800)
x_new = x_new[:,np.newaxis]

x_new_transform = polynomial_features.fit_transform(x_new)
y_new = model.predict(x_new_transform)

# plot the prediction
plt.plot(x_new, y_new, color='blue', linewidth=3)
plt.grid()
plt.xlim(x_new_min,x_new_max)
plt.ylim(0,8000)
title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(meanSquaredError,2), round(r2,2))
plt.title("Prediction of Infection of Covid-19 in Guatemala Enero 2022\n " + title, fontsize=10)
plt.xlabel('Dias')
plt.ylabel('Infectados')
plt.show()