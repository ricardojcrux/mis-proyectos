#!/usr/bin/env python
# coding: utf-8

# ---
# ---
# ---
# ##3 Ejercicio para entregar

# 1. Importe el archivo de datos “*Datos_GrupoXX.dat*” correspondiente a su grupo
#   - Descargue el archivo de Google Drive ([Carpeta "Taller06"](https://drive.google.com/drive/folders/1W9vIQ8hJA_Pgca3j8hO0rxN-z71MUgbK?usp=sharing))  
#   - Copie/Suba el archivo al directorio de trabajo de Colabs (/content/) 
#   - En el encabezado del archivo encontrarán una breve explicación del significado de los datos 
#   - Defina un arreglo de datos usando la función $\texttt{np.loadtxt()}$
# 
# 2. Realice un análisis gráfico de los datos y formule una hipótesis sobre el tipo de relación que se existe entre ellos (*directa*, *inversa*, *exponencial*, *potencial*). Justifique su respuesta
# 
# 3. Verifique su hipótesis realizando las transformaciones necesarias para obtener una gráfica en la que se evidencie una relación lineal entre las variables transformadas ("linealización")
# 
# 4. Utilice el método de regresión lineal para estimar el valor de las constantes del modelo. Indique claramente los valores de estos parámetros con tress cifras decimales y las unidades adecuadas
# 
# 5. Compare gráficamente los datos dados con el modelo obtenido. Discuta sus observaciones 
# 
# 

# 
# 
# **Solución**
# 
# > **Nota**: *Cargar en Campus Virtual un cuaderno que contenga únicamente el enunciado del problema y su solución*

# 
# 
# > - **Solución punto 1:** 

# In[73]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Arreglo de datos recuperado/importado de un archivo
datos_sonido = np.loadtxt('Datos_Grupo01.dat')
datos_x = datos_sonido[:,0]
datos_y = datos_sonido[:,1]


# 
# 
# > - **Solución punto 2:** Viendo la gráfica de los datos podemos tener la certeza de que tienen una proporcionalidad potencial
# 

# In[74]:


# Visualización de los datos originales
plt.title('Datos originales')
plt.plot(datos_x,datos_y,"-o")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# 
# 
# > - **Solución punto 3:** 

# In[75]:


# Cambio de variables y gráfica de los datos transformados
datos_x1 = np.log(datos_x)
datos_y1 = np.log(datos_y)
plt.title('Datos con cambio de variables')
plt.plot(datos_x1,datos_y1,'-*')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
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

# In[82]:


# Regresión entre variables transformadas y parámetros de la regresión
numero_datos =  len(datos_x1)

suma_x = sum(datos_x1)
suma_y = sum(datos_y1)
suma_xx = sum(datos_x1*2)
suma_xy = sum(datos_x1*datos_y1)

denominador = numero_datos * suma_xx - (suma_x**2)

pendiente =  (numero_datos * suma_xy - suma_x * suma_y) / denominador 
intercepto =  (suma_xx * suma_y - suma_xy * suma_x) / denominador

a = (pendiente)
b = np.exp(intercepto)

print(a,b)


# In[93]:


# Evaluación y presentación de los parámetros del modelo
datos_y2 =  b * datos_x ** a
u = np.exp(datos_y2)
plt.title('Modelo propuesto')
plt.plot(datos_x,datos_y2,'-*')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# > - **Solución punto 5**

# In[94]:


# Comparación entre los datos originales y
# las predicciones del modelo

plt.title('Datos en comparativa')
plt.plot(datos_x,datos_y,"-o",label='Datos Originales')
plt.plot(datos_x,datos_y2,'--',label='Modelo Propuesto')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
 

