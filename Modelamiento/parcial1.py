#!/usr/bin/env python
# coding: utf-8

# # IMM - Parcial No 1 (08/11/2022)

# ## Segunda parte - Ejercicio práctico

# 1. Importe el archivo de datos “*Datos_Parcial01_Gr01.dat*”
#   - En el encabezado del archivo encontrarán una breve explicación del significado de los datos 
# 
# 2. Analice los datos gráficamente y formule una hipótesis sobre el tipo de relación matemática que permite modelar adecuadamente la dependencia entre las variables (*directa*, *inversa*, *exponencial*, *potencial*). Justifique su respuesta
# 
# 3. Realice una transformación adecuada de los datos que le permita confirmar si el modelo matemático propuesto es adecuado o no para describir la dependencia entre las variables
# 
# 4. Determine los parámetros del modelo planteado mediante una regresión lineal. Indique claramente los valores de estos parámetros con dos cifras decimales usando notación científica y las unidades adecuadas
# 
# 5. Almacene en el archivo de texto '*Resultados_analisis.dat*' una tabla que contenga los datos de tiempo y temperatura en grados Celsius  correspondientes al rango de 0 a 240 min en pasos de 5 min. Guarde también la gráfica de estos datos junto con los datos originales en un archivo de extensión **png**
# 
# 6. Usando el modelo obtenido, estime la diferencia de temperatura para un tiempo de  2 horas.
# 
# 
# 

# 
# 
# > - **Solución punto 1:** 

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('Datos_Parcial01_Gr01.dat')

datos_x = datos[:,0]
datos_y = datos[:,1]


# 
# 
# > - **Solución punto 2:** 

# In[26]:


plt.plot(datos_x,datos_y,'.')
plt.grid()
plt.show()


# 
# 
# > - **Solución punto 3:** 

# In[25]:


new_x = datos_x
new_y = np.log(datos_y)

plt.plot(new_x,new_y,'.')
plt.grid()
plt.show()


# 
# 
# > - **Solución punto 4**
# 
#  
# 
# 
# 
# 

# In[24]:


import scipy.stats as stat

regresion = stat.linregress(new_x,new_y)

m = regresion.intercept
b = regresion.slope

final_y = m + new_x * b

plt.plot(new_x,new_y, '.', label='Datos con regresión')
plt.plot(new_x,final_y,label='Modelo propuesto')
plt.legend()
plt.grid()
plt.show()


# In[32]:


modelo_y = np.exp(final_y)

plt.plot(datos_x,datos_y, '.', label='Datos originales')
plt.plot(datos_x,modelo_y,label='Modelo propuesto')
plt.legend()
plt.grid()
plt.show()


# > - **Solución punto 5**

# In[48]:


def func(x):
  y1 = m + x * b
  y2 = np.exp(y1)
  return y2

data_x = np.arange(0,100,5)
data_y = np.zeros_like(data_x)

for i in range(len(data_x)):
  data_y[i] = func(data_x[i])

plt.plot(datos_x,datos_y, '.', label='Datos originales')
plt.plot(datos_x,modelo_y,label='Modelo propuesto')
plt.legend()
plt.grid()
plt.show()

plt.plot(datos_x,modelo_y,label='Modelo propuesto')
plt.plot(data_x,data_y,'-o',label='Evaluación de datos')
plt.title('Modelo originales vs Evaluación de datos')
plt.legend()
plt.grid()
plt.savefig('grafico_funcion.png')
plt.show()


# > - **Solución punto 6**

# In[49]:


time = func(120)
print('El estimado de la variación de la temperatura de un objeto comparada con la de su entorno en un lapso de dos horas es: ', time)

