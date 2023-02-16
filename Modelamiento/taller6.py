#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 6 (25/10/2022)

# ## 1. Relaciones de proporcionalidad

# 
# ###1.1 Repaso última sesión
# 
# Acciones realizadas:
# - Recuperación de datos desde un archivo de texto (función $\texttt{loadtxt()}$)
# - Verificación de relaciones de proporcionalidad directa e inversa
# - Evaluación de los coeficientes (pendiente e intercepto) de una regresión lineal
# 
# 

# **1.1.1 Ejercicio anterior: Proporcionalidad inversa**
# 
# 
# > 1. Recupere los datos contenidos en el archivo “*datos_proporcion.dat*”. 
#   - Descargue el archivo de Google Drive ([Carpeta "Taller05"](https://drive.google.com/drive/folders/1PP-0T_A9A1BdJkZqLnkzLDNGcdB9K5Fc?usp=sharing))
#   - Copie/Suba el archivo al directorio de trabajo de Colabs (/content/) 
#   - Lea los datos usando la función $\texttt{np.loadtxt()}$
# 2. Grafique los datos y establezca si la relación de proporcionalidad entre ellos es *directa* ($y = a\cdot x$) o *inversa* ($y = a / x$)
# 3. Determine el valor de la constante de proporcionalidad  $a$
# 4. En la misma gráfica muestre los datos leidos y  el resultado de la relación de proporcionalidad encontrada 
# 
# 

# 
# 
# > - **Solución primer punto:**
# 
# 

# In[ ]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Arreglo de datos recuperado/importado de un archivo
#datos_archivo = np.loadtxt('datos_proporcion.dat')
# Arreglo de datos definido directamente
datos_archivo = np.array([[1.0, 3.27857673], [1.47368421, 2.22949735], [1.94736842, 1.67941768], [2.42105263, 1.34075362], [2.89473684, 1.11086645], [3.36842105, 0.92764479], [3.84210526, 0.88333579], [4.31578947, 0.78443255], [4.78947368,  0.63890552], [5.26315789, 0.60346056], [5.73684211, 0.60466256], [6.21052632, 0.50890251], [6.68421053, 0.50964695], [7.15789474, 0.43846083], [7.63157895, 0.42106615], [8.10526316, 0.38587242], [8.57894737, 0.33770211], [9.05263158, 0.32257995], [9.52631579, 0.38837135], [10., 0.2908778]])

# Variables a analizar
datos_x = datos_archivo[:,0] # Primera columna
datos_y = datos_archivo[:,1] # Segunda columna


# 
# 
# > - **Solución segundo punto:**
# 
# 

# In[ ]:


# Visualización de las variables 

plt.style.use ('default')
plt.figure(figsize = (5,2.8)) 
plt.plot(datos_x,datos_y,'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# 
# 
# > - **Solución tercer punto:**
# 
# 

# In[ ]:


# Para relación inversa x*y = cte 
datos_a = datos_x*datos_y

# Se evalúa el promedio de los distintos valores a = x*y
a_prom = np.mean(datos_a)
print('Valor estimado de la constante: a_prom = %6.3f ' % a_prom, '\n')

plt.figure(figsize = (5,2.8)) 
plt.style.use ('default')
plt.plot(datos_x,datos_a,'o',label='a = x*y')
plt.plot(datos_x,a_prom*np.ones(len(datos_a)),'-',label='promedio')

plt.xlabel('x')
plt.ylabel('y * x')
plt.grid()
plt.legend()
plt.show()


# 
# 
# > - **Solución punto 4:**
# 
# 

# In[ ]:


# Comparación entre los datos y el modelo matemático

datos_y_promedio  = a_prom / datos_x

plt.style.use ('default')
plt.figure(figsize = (5,2.8)) 
plt.plot(datos_x,datos_y,'o',label='datos')
plt.plot(datos_x,datos_y_promedio,'-',label='y = a/x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()


# ---
# ---
# 
# **1.1.2 Repaso de regresión**
# 
# 
# **Definición**: técnica de modelado estadístico que se utiliza para describir una *variable de respuesta* en función de una o más *variables predictoras*. 
# 
# - En una *regresión lineal simple* se utiliza un predictor $x$ para describir una variable de respuesta $y$,   a través de la ecuación general
# $$y = \beta_0 + \beta_1\,x$$
# 
# - Los parámetros $\beta_0$ (*intercepto*) y $\beta_1$ (*pendiente*, *razón de cambio*) son los *parámetros del modelo* 
# 
# - Los parámetros del modelo se evalúan a partir del conjunto de datos disponibles $\{(x_i,y_i),\,i=1,\dots,n\}$
# 
# **Estimación de los parámetros**: La estimación de $\beta_0$ y $\beta_1$ se realiza mediante el *método de mínimos cuadrados*
#   - Valor estimado del intercepto: 
#     $$\beta_0  \equiv b = \frac{S_{xx}\cdot S_y  - S_{xy}\cdot S_x }{n\cdot S_ {xx} - S_x^2  } $$
# 
#   - Valor estimado de la pendiente:
#   $$\beta_1   \equiv m =  \frac{n\cdot S_{xy} - S_x\cdot S_y }{n\cdot S_{xx}- S_x^2} $$
# 
#   - Las sumatorias $S$ dependen de los datos disponibles
#   $$ S_x = \sum_{i=1}^{n} x_i, \qquad S_y =   \sum_{i=1}^{n} y_i,  \qquad S_{xx} = \sum_{i=1}^{n} x_i^2,  \qquad S_{xy} = \sum_{i=1}^{n} x_i y_i, $$
# 
#   - Nota: Dependiendo de la naturaleza de las variales $x$ y $y$, los parámetros del modelo tendrán unidades de medida adecuadas

# ---
# ---
# ##2. Modelos de ajuste exponencial y de potencia
# 
# - El procesamiento e interpretación de datos experimentales es una tarea muy importante en el proceso de investigación científica. Una vez que se recopilan los datos, surgen preguntas como las siguientes: 
#   - ¿Los datos son "creíbles"? Es decir, los datos no muestran  signos evidentes de un instrumento mal calibrado o de un protocolo experimental deficiente.
#   - ¿Cómo se pueden cuantificar las relaciones entre las variables involucradas en un conjunto de datos?
#   - Una vez que se cuantifica una relación entre variables, *¿cómo se puede usar esa información para hacer predicciones más allá de lo que se puedo medir experimentalmente (interpolación y extrapolación)*?
# 
# - Suponiendo que la respuesta a la primera pregunta es afirmativa, el procedimiento conocido como *análisis de regresión* permite  abordar las otras dos preguntas.
# 
# - En esta sección se consideran  tipos especiales de relaciones matemáticas entre dos variables, $y = f(x)$, cuyos parámetros pueden evaluarse fácilmente empleando el procedimiento ya estudiado de regresión lineal. 
#    - Modelo exponencial: $$ y = b\cdot {\rm e}^{a\cdot x} = b\cdot \exp(a\cdot x) $$
#    - Modelo de potencia:: $$ y = b \cdot x^a$$
# - La regresión lineal se puede aplicar en estos casos realizando *cambios adecuados* a las variables $x$ o $y$   

# ---
# ---
# ### 2.1 Transformación de variables: linealización
# 
# 
# Para solucionar el ejercicio anterior sobre proporción inversa, es decir, 
# $$y= \frac{a}{x},$$ 
# se puede realizar el cambio de variable  
# $$z = \frac{1}{x}.$$
# De esta manera, la relación entre $y$ y $z$ se vuelve lineal
# $$y = a \cdot z,$$
# y el estimado de la constante $a$ se puede evaluar como la pendiente de una regresión lineal aplicada a los datos $(z,y)$

# 
# 
# > - **Transformación de variables**
# 
# 

# In[ ]:


# Cambio de variable
datos_z = 1 / datos_x

# Grafica las dos listas de valores
plt.style.use ('default')
plt.figure(figsize = (5,2.8)) 
plt.plot(datos_z, datos_y, '-o')
plt.xlabel(' ')
plt.ylabel(' ')
plt.title(' ')
plt.grid()
plt.show()


# 
# 
# > - **Regresión entre las variables transformadas**
# 
# 

# In[ ]:


# Realiza la regresión entre z e y

numero_datos =  len(datos_z)
# Sumas
suma_x,suma_y,suma_xx,suma_xy = 0,0,0,0

for i in range(numero_datos):
  suma_x  += datos_z[i]
  suma_y  += datos_y[i] 
  suma_xx += datos_z[i]*2
  suma_xy += datos_z[i]*datos_y[i]

denominador = numero_datos * suma_xx - (suma_x)**2

# Parámetros del modelo 
pendiente  =  (suma_xx * suma_y - suma_xy * suma_x) / denominador
intercepto =  (numero_datos * suma_xy - suma_x * suma_y) / denominador
print(pendiente,intercepto)


# 
# 
# > - **Resultado del análisis**
# 
# 

# In[ ]:


# Estimación de la constante de proporcionalidad 

a_reg = suma_x / suma_y
print('Valor estimado de la constante: a_reg = %6.3f ' % a_reg, '\n')

datos_y_regresion =  a_reg * datos_x

plt.figure(figsize = (5,2.8)) 
plt.style.use ('default')
plt.plot(datos_x,datos_y,'o',label='datos')
plt.plot(datos_x,datos_y_regresion,'-',label='regresión')
plt.plot(datos_x,datos_y_promedio,'--',label='promedio')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = a/x')
plt.grid()
plt.legend()
plt.show()


# ---
# ---
# 
# 
# 
# ###2.2 Proporcionalidad exponencial
# 
# - Una relación exponencial entre dos variables $x$ e $y$ es aquella que se puede expresar como 
# 
#  $$y = b\cdot {\rm e}^{a\cdot x}= b\cdot \exp(a\cdot x),$$
# 
#  donde  $a$ y $b$ son valores constantes (*parámetros del modelo*).
# 
# - Empleando logaritmo natural a lado y lado de una relación exponencial  es posible extraer una relación lineal 
# 
#  $${\color{red}{\ln(y)}} = {\color{blue}{\ln(b)}} + a\cdot x    $$
# 
#  $${\color{red} Y} = {\color{blue}B} + a\cdot x$$
# 
# - A partir de un análisis de regresión lineal de los datos $(x, Y)$ se puede estimar tanto $a$ como $b=\exp(B)$ 
# 
# - Un ejemplo del uso de relaciones exponenciales es la descripción del comportamiento temporal de la concentración $\mathcal{A}$ de una especie química $A$ en una reacción de primer orden ($A \to B$).  En tal caso, la expresión
# $$ \mathcal{A} = \mathcal{A}_0\, {\rm e}^{-k\,t},$$
# describe cómo cambia la concentración de $A$ en el tiempo,  siendo $\mathcal{A}_0$ su concentración inicial y $k$ la velocidad de reacción.
# 

# ---
# ---
# ###2.3 Proporcionalidad de potencia (proporcionalidad potencial)
# 
# - Una relación de "ley de potencia" entre dos variables $x$ e $y$ es aquella que se puede expresar como 
# 
#  $$y = b\cdot x^a,$$
# 
#  donde las constantes $a$ y $b$ se denominan,  respectivamente, exponente (o potencia) y constante de proporcionalidad.
# 
# - Empleando logaritmo a lado y lado de una relación de potencia  es posible extraer una relación lineal 
# 
#  $${\color{white}{....}} {\color{red}{\ln(y)}} = {\color{blue}{\ln(b)}} + a\cdot {\color{green}{\ln(x)}}   $$
# 
#  $${\color{red} Y} = {\color{blue}B} + a\cdot {\color{green} X}$$
# 
# - A partir de un análisis de regresión lineal de los datos $(X, Y)$ se puede estimar tanto $a$ como $b=\exp(B)$ 
# 
# - Un ejemplo sencillo de este tipo de relaciones surge al analizar el área $A$ de un círculo, que se expresa como
# $$A = \pi\,r^2,$$
# donde $r$ representa el radio del círculo. En este caso, la constante de proporcionalidad es igual a $\pi$ y el exponente es igual a 2.

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

# In[16]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat

# Arreglo de datos recuperado/importado de un archivo
datos_sonido = np.loadtxt('Datos_Grupo01.dat')
datos_x = datos_sonido[:,0]
datos_y = datos_sonido[:,1]


# 
# 
# > - **Solución punto 2:** Viendo la gráfica de los datos podemos tener la certeza de que tienen una proporcionalidad potencial
# 

# In[17]:


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

# In[18]:


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

# In[24]:


# Regresión entre variables transformadas y parámetros de la regresión
star = stat.linregress(datos_x1,datos_y1)
m = star.intercept
b = star.slope
print(m,b)


# In[28]:


# Evaluación y presentación de los parámetros del modelo
datos_y2 = m + datos_x1 * b
plt.title('Datos con regresión')
plt.plot(datos_x1,datos_y2,'-',color='red',label='Modelo Propuesto')
plt.plot(datos_x1,datos_y1,'-*',label='Datos con regresion')
plt.legend()
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.grid()
plt.show()


# > - **Solución punto 5**

# In[30]:


# Comparación entre los datos originales y
# las predicciones del modelo
y2 = np.exp(datos_y2)
plt.title('Datos en comparativa')
plt.plot(datos_x,datos_y,"-o",label='Originales')
plt.plot(datos_x,y2,'--',color='red',label='Regresión')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
 

