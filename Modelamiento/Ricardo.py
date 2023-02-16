#!/usr/bin/env python
# coding: utf-8

# ---
# ---
# ---
# ##3 Ejercicio para entregar

# Con la ayuda de las leyes de Newton se puede modelar matemáticamente el movimiento de un péndulo simple. Una de las consecuencias más importantes de este modelo es que el periodo de oscilación $T$ del péndulo está determinado por su longitud $L$ mediante la siguiente expresión matemática:
# 
# $$ T = 2 \pi \sqrt{\dfrac{L}{g}},$$
# 
# donde $g$ corresponde a la constante de la aceleración de la gravedad. 
# 
# **Problema**: En un experimento se midió el periodo de un péndulo simple para diferentes longitudes
# y se obtuvo el siguiente conjunto de datos.
# 
# $$
# \begin{aligned}
# &\begin{array}{|c|c|}
# \hline \hline \text {Longitud (m)} & \text {Periodo (s)} \\
# \hline 0.10 & 0.65   \\
# 0.17 & 0.79   \\
# 0.20 & 0.90   \\
# 0.25 & 1.01  \\
# 0.26 & 1.10  \\
# 0.32 & 1.20   \\
# 0.40 & 1.27   \\
# 0.49 & 1.34   \\
# 0.50 & 1.42  \\
# 0.58 & 1.50   \\
# 0.60 & 1.55   \\
# \hline
# \end{array}
# \end{aligned}
# $$
# 
# Con base en la información anterior, realice las siguientes tareas:
# 
# 1. Proponga un cambio de variable $Y=F(T)$ y $X=G(L)$ que le permita tener un modelo lineal, $Y = m\,X+b$, a partir de los datos experimentales. Grafique los datos originales, así como los datos transformados.
# 
# 2. A partir de una regresión lineal de los datos transformados, estime el valor de la constante de la aceleración de la gravedad $g$.
#  
# 3. Usando el modelo obtenido, estime el periodo de un péndulo de longitud 2500 mm.
# 
# 4. Encuentre el polinomio interpolante de Lagrange que pasa por los primeros cuatro pares de datos y muestre su gráfico. 
# 
# 5. Compare el valor del periodo un péndulo de 15 centímetros que se obtiene utilizando el polinomio interpolante y el modelo de regresión lineal. Explique cuál predicción es más confiable.
# 
# 6. De manera similar al punto anterior, compare el valor del periodo un péndulo de 60 centímetros usando el polinomio interpolante y el modelo de regresión lineal. Explique cuál predicción es más confiable en este caso.
# 
# **Nota:** Subir a campus virtual un cuaderno con solo el planteamiento del problema y su solución

# * **Solución punto 1:** Transformación de datos

# In[3]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Datos originales
longitud  = np.array([0.10, 0.17, 0.20, 0.25, 0.26, 0.32, 0.40, 0.49, 0.50, 0.58, 0.60])
periodo   = np.array([0.65, 0.79, 0.90, 1.01, 1.10, 1.20, 1.27, 1.34, 1.42, 1.50, 1.55])


# > Cambios de variable para linealizar el modelo:
# 
# $$ X = $$
# 
# $$ Y = $$
# 

# In[14]:


# cambio de variable
variable_x = (longitud)
variable_y = (periodo)

plt.plot(longitud,periodo,'o')
plt.plot(variable_x,variable_y)
plt.show()


# * **Solución punto 2:** Regresión lineal para estimar $m$

# In[ ]:






# * **Solución punto 3:** Estimación del periodo para una longitud de 2500 mm 

# In[ ]:






# * **Solución punto 4:** Interpolación para las cuatro primeras parejas de datos  

# In[ ]:




 


# * **Solución punto 5:** Estimación del periodo para una longitud de 15 cm 

# In[ ]:






# * **Solución punto 6:** Estimación del periodo para una longitud de 50 cm

# In[ ]:





