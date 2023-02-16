#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importamos las librerias numpy y matplotlib
import numpy as np
import matplotlib.pyplot as plt

#importamos el archivo datos.dat
datos= np.loadtxt('datos.dat')
print(datos)
#utilizamos las filas de los datos importados
x1= datos[:,0]
y1= datos[:,1]

#graficamos los valores del archivo
plt.plot(x1,y1,'or-',color='red')
plt.grid()
plt.show()
print('')

#por la grafica se observa que es una proporcionalidad inversa
print('Es una proporcionalidad inversa')

#calculamos el valor de la constante de la proporcionalidad inversa
k=0
for i in range(len(x1)):
  ki= x1[i]*y1[i]
  k+=ki
cons=k/(len(x1))
print('La constante de la proporcionalidad inversa es: ',cons,'\n')

#reescalamos el eje x a 1/x con una función
def f(x):
  return 1/x
x2= f(x1)

#graficamos con los nuevos valores 1/x y y
plt.plot(x2,y1,color='blue')
plt.grid()
plt.show()



