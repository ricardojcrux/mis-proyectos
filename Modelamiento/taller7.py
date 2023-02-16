#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 7 (08/11/2022)

# ---
# ---
# ##1. Repaso regresión lineal

# ### 1.1 Definición: 
# 
# Técnica de modelado estadístico que se utiliza para describir una *variable de respuesta* en función de una o más *variables predictoras*. 
# 
# - En una *regresión lineal simple* se utiliza un predictor $x$ para describir una variable de respuesta $y$,   a través de la ecuación general
# $$y = \beta_0 + \beta_1\,x$$
# 
# - Los parámetros $\beta_0$ (*intercepto*) y $\beta_1$ (*pendiente*, *razón de cambio*) son los *parámetros de regresión* 
# 
# - Los parámetros de regresión se evalúan a partir del conjunto de datos disponibles $\{(x_i,y_i),\,i=1,\dots,n\}$
# 
# - **Estimación de los parámetros**: La estimación de $\beta_0$ y $\beta_1$ se realiza mediante el *método de mínimos cuadrados*

# ###1.2. Cambios de variable - Modelos de ajuste exponencial y de potencia
# 
# **1.2.1 Relación exponencial**
# 
# - La relación entre las variables $x$ e $y$ se puede expresar como 
# 
#  $$y = b\cdot {\rm e}^{a\cdot x}= b\cdot \exp(a\cdot x),$$
# 
#  donde  $a$ y $b$ son valores constantes (*parámetros del modelo*).
# 
# - Transformado las variables es posible extraer una relación lineal 
# 
#  $${\color{red}{\ln(y)}} = {\color{blue}{\ln(b)}} + a\cdot x    $$
# 
#  $${\color{red} Y} = {\color{blue}B} + a\cdot x$$
# 
# - Con un análisis de regresión lineal de los datos $(x, Y)$ se pueden estimar   $a$ y $b$ a partir de la pendiente y el intercepto de la recta ajustada
# 
# **1.2.1 Relación potencial**
# 
# - La relación entre las variables $x$ e $y$ se puede expresar como 
# 
#  $$y = b\cdot x^a,$$
# 
#  donde $a$ y $b$ son valores constantes (*parámetros del modelo*).
# 
# - Transformado las variables es posible extraer una relación lineal 
# 
#  $${\color{red}{\ln(y)}} = {\color{blue}{\ln(b)}} + a\cdot {\color{green}{\ln(x)}}    $$
# 
#  $${\color{red} Y} = {\color{blue}B} + a\cdot  {\color{green}X}$$
# 
# - Con un análisis de regresión lineal de los datos $(X, Y)$ se pueden estimar los parámetros del modelos $a$ y $b$ a partir de la pendiente y el intercepto de la recta ajustada
# 

# ---
# ---
# ---
# ## 2. Interpolación de Lagrange
# 
# 

# ### 2.1 Definición
# 
# Suponga que se tiene una serie de datos (observaciones)
#  
#  $$\{(x_j, y_j), j=0,1,\dots,n \},$$
# 
#  con $x_j \ne x_i$ si $j\ne i$ (es decir, todos los valores de $x$ son distintos).
# 
# - Para modelar dichos datos, se quiere encontrar una función que permita establecer una relación $y = f(x)$ entre ellos, **restringida a la condición $y_i=f(x_i)$ para todo $i$**
# 
# - Tal función se puede construir usando la técnica de [*interpolación polinomial*](https://es.wikipedia.org/wiki/Interpolaci%C3%B3n_polin%C3%B3mica), en la que $f(x)$ es un polinomio de grado $n$, es decir,
# 
#  $$f(x) = a_0 + a_1 x + a_2 x^2 +\dots + a_n x^n $$ 
# 
# - Una de estas técnicas hace uso del *polinomio interpolante en la forma de Lagrange* $P(x)$, definido como
# 
#  $$P(x) = \sum_{j=0}^n\, y_j \cdot  L_j(x)$$
#  
#   donde $L_j(x)$ representa la *base polinómica de Lagrange*
# 
# - Esta base a su vez se define a partir de los datos usando la expresión
# 
#  $$L_j(x) = \prod_{i=0,\,i\ne j}^n \frac{x-x_i}{x_j-x_i}$$
# 
# 

# ---
# ### 2.2 Ejemplo de evaluación del "polinómio interpolante" 
# 

# **Problema:** Dado el conjunto de datos presentado en la tabla, evalúe el polinomio interpolante correspondiente usando el método de Lagrange. 
# 
# | x | | y
# |-------| |-----------
# |-2.0 | |  6.1
# |-1.0 | |  5.4
# | 0.0 | |  4.2
# | 1.0 | | -2.0
# | 2.0 | | -1.5
# | 3.0 | |  1.4
# 
# **Solución:** Para solucionar este problema se deben seguir tres pasos:
# - Definir una función que evalúe la base de Lagrange (ver [diagrama de flujo](https://drive.google.com/file/d/1lPqGFC12gWvmdi59INeB-kBnV5hqQuxN/view?usp=share_link))
# - Definir una función que construya el polinomio interpolante (ver [diagrama de flujo](https://drive.google.com/file/d/1GUpdQK5vj5Ttv7iHFFj7y-Pc2zWBihep/view?usp=share_link))
# - Aplicar a los datos correspondientes 

# **2.2.1 Solución usando funciones definidas por el usuario**
# 
# 
# 
# 
# 

# In[ ]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
# Define el estilo y tamaño de las gráficas
plt.style.use ('default')
#plt.style.use ('seaborn-poster')
plt.rcParams['figure.figsize'] = [5, 2.8]


# - **Primer paso: definición de la base de Lagrange**
# 
# 

# In[119]:


def base_lagrange(x, x_datos, j):
  Lj = 1
  for i in range(len(x_datos)):
    if i != j:
      Lj = Lj * (x-x_datos[i])/(x_datos[j]-x_datos[i])
  return Lj


# - **Segundo paso: construcción del polinomio interpolante**

# In[120]:


def polinomio_interpolador(x, x_datos, y_datos):
  poly = 0
  for j in range(len(x_datos)):
    poly += y_datos[j]*base_lagrange(x,x_datos,j) 
  return poly


# - **Tercer paso: aplicación a los datos dados**

# In[121]:


# Datos de las variables
x_datos = np.array([-2.0, -1.0, 0.0,  1.0,  2.0, 3.0])
y_datos = np.array([ 6.1,  5.4, 4.2, -2.0, -1.5, 1.4])

# Valores de x para evaluar el polinomio interpolante 
# (función definida por el usuario)
xmin = np.min(x_datos)
xmax = np.max(x_datos)
x_interpolacion = np.linspace(xmin,xmax,100)
y_interpolacion = polinomio_interpolador(x_interpolacion,x_datos,y_datos)

# Visualización de los datos
plt.plot(x_datos,y_datos,'s',label='datos')
plt.plot(x_interpolacion, y_interpolacion,'-',label='interpolación')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


# **2.2.1 Solución usando funciones predeterminadas (librería *SciPy)***
# 

# In[122]:


# Empleando herramientas predefinidas en la librería scipy
import scipy.interpolate as spy

# Primer y segundo pasos: Evalúa los coeficientes (base) del polinomio interpolador
polinomio_de_lagrange = spy.lagrange(x_datos, y_datos)
# Tercer paso: Evalúa el polinomio interpolador para x_interpolacion
y_interpolacion_spy = polinomio_de_lagrange(x_interpolacion)

# Visualización
plt.plot(x_datos,y_datos,'s',label='datos')
plt.plot(x_interpolacion, y_interpolacion, '-', label='usuario')
plt.plot(x_interpolacion, y_interpolacion_spy, '.', label='scipy')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


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

# In[ ]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Datos originales
longitud  = np.array([0.10, 0.17, 0.20, 0.25, 0.26, 0.32, 0.40, 0.49, 0.50, 0.58, 0.60])
periodo   = np.array([0.65, 0.79, 0.90, 1.01, 1.10, 1.20, 1.27, 1.34, 1.42, 1.50, 1.55])


# > Cambios de variable para linealizar el modelo:
# 
# $$ X = ???$$
# 
# $$ Y = ???$$
# 

# In[ ]:


# cambio de variable
variable_X = ????
variable_Y = ????
  



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





