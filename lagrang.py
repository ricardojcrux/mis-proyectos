import numpy as np
from scipy.interpolate import lagrange

x = np.array([0, 1, 2])
y = x**3

#Teniendo el polinomio interpolante de Lagrange
poly = lagrange(x, y)

#Sacando la derivada
dpoly = poly.deriv(1)

#podemos imprimier las expresiones
print(poly)
print(poly.coef)
print(dpoly)