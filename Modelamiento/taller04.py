#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 4 (11/10/2022)

# ## 1. Elementos básicos de python
# 
# 
# - *Sintaxis*: comandos, identación (sangría)
# - *Variables*: variables lógicas, listas (indexación, concatenación)
# - *Estructuras condicionales*: $\texttt{if}\dots\texttt{elif}\dots\texttt{else}$
# - *Estructuras cíclicas*: $\texttt{for}$, $\texttt{while}$ 
# - *Funciones*: definición y llamado
# - *Gráficos*: módulo gráfico $\texttt{matplotlib.pyplot}$

# ---
# ---
# ###1.1 Repaso última sesión
# 
# **1.1.1 Funciones, librerías y módulos**
# 
# 
# - En python, ¿qué es una función predeterminada?
# - En python, ¿qué es una función definida por el usuario?
# - ¿Cuál es el propósito de usar librerías y módulos?
# 
# **1.1.2 Gráficos usando el módulo $\texttt{matplotlib.pyplot}$**
# 
# 
# Un recipiente con cierta cantidad de hielo se puso  sobre una placa calefactora y se procedió a medir su temperatura $T$ (°C) en función del tiempo $t$ (min). El comportamiento obtenido se puede modelar adecuadamente con la función:
# 
# $$T(t) = \begin{cases}
# 2(t - 10) & 0 \le t < 10 \\
# 0       & 10 \le t < 20 \\
# \frac{20}{3}(t - 20) & 20 \le t < 35 \\
# 100 & 35 \le t \le 50 \\
# \end{cases}$$
# 
# *Problema:*
# 
# Grafique la función $T(t)$ en el intervalo indicado

# *Solución:*
# 
# - Paso 1: Definir la función que se quiere graficar
# - Paso 2: Generar las listas de datos a graficar
# - Paso 3: Realizar la gráfica importando el módulo $\texttt{pyplot}$

# In[8]:


# Paso 1 
# Define la funcion a graficar

def funcion_temperatura(tiempo):
  if (0 <= tiempo and tiempo < 10):
    temperatura = 2*(tiempo-10)
  elif (10 <= tiempo and tiempo < 20):  
    temperatura = 0
  elif (20 <= tiempo and tiempo < 35):  
    temperatura = 20*(tiempo-20)/3
  elif (35 <= tiempo and tiempo <= 50):  
    temperatura = 100
  else:    
    temperatura = []
  return temperatura


# In[9]:


# Paso 2
# Define las listas de datos

# Lista de Tiempo
lista_tiempo = list(range(0,51))

# Lista de Temperatura
lista_temperatura = []
for tiempo in lista_tiempo:
  temperatura = funcion_temperatura(tiempo)
  lista_temperatura += [temperatura]


# In[10]:


# Paso3
# Grafica las listas de datos

# Lllama al módulo pyplot
import matplotlib.pyplot as plt

plt.plot( lista_tiempo, lista_temperatura, '*-' ) 
# Algunos atributos de la gráfica
plt.xlabel('Tiempo (min)')
plt.ylabel('Temperatura (°C)')
plt.title('Gráfico de T vs t')
plt.grid()
# Muestra la figura resultante
plt.show()


# ---
# ---
# ###1.2 La librería $\texttt{numpy}$
# 
# **1.2.1 Definición**
# 
# *NumPy* (*Numerical Python*) es una librería de Python especializada en el cálculo y el análisis de datos numéricos (https://numpy.org/)
# 
# - nueva clase de objetos $\to$ *arrays* (arreglos)
# - suponga las listas 
#   ```
#   a = [1, 2, 3, 4]
#   b = [1, 4, 9, 16]
#   ```
#   ¿Cómo se puede obtener la lista $\texttt{b}$ a partir de la lista $\texttt{a}$?
# 
# 
# 

# In[11]:


# Muestra información de la librería numpy instalada usando
# el gestor de paquetes "pip" (python installer packages)

get_ipython().system(' pip show numpy')


# **1.2.2 Arreglos (*Arrays*)**
# 
# - un *array* es una colección de datos numéricos en múltiples dimensiones (vector, matriz, cubo,...)
# - *NumPy* incorpora funciones muy eficientes para realizar diversas operaciones matemáticas entre   *arrays* (álgebra lineal)
# - listas $\leftrightarrow$ arreglos
#  - las dos son colecciones de elementos contenidos en una única variable
#  - dichos elementos son mutables e indexables
#  - listas 
#    - pueden contener distintos tipos de elementos  
#  - arreglos 
#    - solo puede contener elementos numéricos 
#    - almacenamiento y manipulación más eficientes
# 
# 
# 
# 
# 
# 

# <font size=1> Imagen tomada de: https://aprendeconalf.es/docencia/python/manual/numpy </font>
# 
# <img src=https://aprendeconalf.es/docencia/python/manual/img/arrays.png  width=400>

# - un ejemplo del uso de arreglos 3D es el almacenamiento de datos en las tomografías
# 

# <font size=1> Imagen tomada de: https://www.qualitymag.com/articles/94885-ct-inspection-an-inside-look-at-ct-based-nondestructive-testing  </font>
# 
# <img src= https://www.qualitymag.com/ext/resources/Issues/2018/August/NDT/ct-inspection/Computed-Tomography-Principle.jpg  width=450>

# **1.2.3 Ejemplos del uso de arreglos de $\texttt{numpy}$**

# - Tipo de variable

# In[12]:


# Importa la librería numpy con el alias "np"

import numpy as np

# Lista de numeros
mi_lista = [1, 2, 4, 6]
print(type(mi_lista))

# Arreglo de numpy
mi_arreglo = np.array([1, 2, 4, 6])
print(type(mi_arreglo))


# - Diferencias entre arreglos y listas

# In[13]:


# Diferencias

print('Suma de dos listas   = ', mi_lista + mi_lista)
print('Suma de dos arreglos = ', mi_arreglo + mi_arreglo,'\n')

print('Producto de un número con una lista  = ', 3*mi_lista)
print('Producto de un número con un arreglo = ', 3*mi_arreglo,'\n')

print('Producto de dos listas   = ', 'PRODUCE ERROR')
print('Producto de dos arreglos = ', mi_arreglo*mi_arreglo)


# - Indexación

# In[14]:


# Indexación

arreglo_0 = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

print('Arreglo =', arreglo_0,'\n')

print('Primer elemento del arreglo =', arreglo_0[0],'\n')
print('Tercer elemento del arreglo =', arreglo_0[2],'\n')
print('Último elemento del arreglo =', arreglo_0[-1],'\n')


# **1.2.3 Creación de arreglos**
# 
# - A través de listas  
#   - $\texttt{np.array( lista_dada )}$
# - A través de funciones predeterminadas
#   - $\texttt{np.linspace(inicio, fin, num_puntos)}$
#   - $\texttt{np.arange(inicio, fin, paso)}$
#   - $\texttt{np.zeros(num_elementos)}$
#   - $\texttt{np.ones(num_elementos)}$
#   - $\texttt{np.zeros_like(arreglo)}$
#   - $\texttt{np.ones_like(arreglo)}$
# 

# In[15]:


import numpy as np

# Generar un arreglo de forma automática 
print('Generación de arreglos de forma automática:\n')

arreglo_1 = np.linspace(-10, 10, 21)
print('arreglo_1 = ', arreglo_1, '\n')

arreglo_2 = np.arange(-10, 10,3)
print('arreglo_2 = ', arreglo_2, '\n')

arreglo_3 = np.zeros(5)
print('arreglo_3 = ', arreglo_3, '\n')

arreglo_4 = np.ones(7)
print('arreglo_4 = ', arreglo_4, '\n')

arreglo_5 = np.zeros_like(arreglo_4)
print('arreglo_5 = ', arreglo_5)

arreglo_6 = np.ones_like(arreglo_2)
print('arreglo_6 = ', arreglo_6)


# **1.2.4 Funciones con arreglos**
# 
# - NumPy suministra un gran número de [funciones predeterminadas](https://numpy.org/doc/stable/reference/routines.math.html) útiles para el cálculo numérico
# 
# 

# In[16]:


import numpy as np

# Funciones trigonométricas
theta = np.linspace(0, np.pi, 4)
print('* Funciones trigonométricas:\n')
print('theta      = ', theta)
print('sin(theta) = ', np.sin(theta))
print('cos(theta) = ', np.cos(theta))
print('\n')

# Funciones exponencial y logaritmica
x = np.arange(1, 2.5, 0.4)
print('* Funciones exponencial y logaritmo natural:\n')
print('x      =', x)
print('exp(x) =', np.exp(x))
print('ln(x)  =', np.log(x))


# - También se pueden usar funciones definidas por el usuario

# In[17]:


# Función definida por el usuario
import numpy as np

def mi_funcion(x):      
  fx = np.sin(x) + np.cos(x) 
  return fx  

arreglo_x = np.linspace(0, 5, 5)
arreglo_y = mi_funcion(arreglo_x)

print('* Función definida por el usuario:\n')
print('  x  = ', arreglo_x)
print('f(x) = ', arreglo_y)


# ---
# ---
# ###1.3 Gráficas usando arreglos
# 
# 
# **Ejemplo**: Realizar el gráfico de las funciones $\sin(x)$ y $\cos(x)$ para $0 \le x \le 2 \pi$.
# 

# **Solución:**
# 
# - Generar los datos a graficar

# In[18]:


# Importa las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# Valores de la variable independiente 
# como un arreglo de la librería numpy
#--------------------------------------------
arreglo_x = np.linspace(-np.pi,np.pi,100)
# Valores de las variables dependientes 
# como arreglos
#--------------------------------------------
arreglo_sen = np.sin(arreglo_x)
arreglo_cos = np.cos(arreglo_x)

# Mostrar los primeros 5 elementos de los arreglos
print('* Los valores de     x  son: ', arreglo_x[0:5], '...')
print('* Los valores de sin(x) son: ', arreglo_sen[0:5], '...')
print('* Los valores de cos(x) son: ', arreglo_cos[0:5], '...')


# - Generar las gráficas 
#   - [ejemplos de estilos de gráficas](https://medium.com/analytics-vidhya/create-your-custom-matplotlib-style-701f0e080250)
#   - [ejemplos de estilos de línea](https://www.geeksforgeeks.org/line-plot-styles-in-matplotlib/)

# In[37]:


# Ajusta el tamaño de la figura (ancho y alto)
plt.figure(figsize = (8,5)) 
plt.style.use('default')
#plt.style.use ('seaborn-poster')

# Grafica los arreglos de datos
plt.plot(arreglo_x, arreglo_sen, 'o:r', label= 'sin(x)')
plt.plot(arreglo_x, arreglo_cos, 's:b', label= 'cos(x)')

# Agrega nombres a los ejes
plt.xlabel('x')
plt.ylabel('y = f(x)')

# Agrega título, leyenda y mallado
plt.title('Funciones sen(x) y cos(x)')
plt.legend()
plt.grid()
 
# Muestra el gráfico
plt.show()


# ---
# ---
# ###1.4 Guardar datos y gráficas en archivos
# 
#  
# 
# 
# Normalmente, el resultado de realizar tareas en las que se procesa información es un arreglo que contiene datos o una gráfica que los muestra. Es entonces de interés el poder almacenar esa información para su uso posterior.
# 
# **Ejemplo**: se quiere  evaluar la función $f(x)=\cos(x^2)$ para sesenta valores de $x$ en el intervalo $[0,3]$ y  guardar los datos correspondientes en un archivo de texto

# **1.4.1 Generar los datos a guardar**
# 
# 
# 
# 
# 

# In[38]:


# Evalua una función matemática y el arreglo generado
# se exporta a un archivo de texto plano
import numpy as np

# Define el arreglo de la variable x
datos_x = np.linspace(-2*np.pi,2*np.pi,100)

# Evalua el arreglo de interés
datos_y =  np.sin(datos_x)

# Prepara un arreglo con los datos en columnas para 
# ser almacenados
datos_dos_columnas = np.column_stack( (datos_x, datos_y) )
print('datos_dos_columnas \n\n', datos_dos_columnas[0:6,:],'... \n')


# **1.4.2 Almacena los datos a un archivo**
# 
# 

# La estructura $\texttt{numpy.savetxt(nombre_archivo, nombre_arreglo, delimiter = '\t')}$ permite guardar un arreglo en un archivo de texto separando las columnas por tabulaciones.
# 
# - Ver formato CSV: https://es.wikipedia.org/wiki/Valores_separados_por_comas
# - Ver estructura $\texttt{numpy.savetxt()}$ : https://interactivechaos.com/en/node/497
# 
# 
# El archivo guardado con la estructura anterior queda localizado de la siguiente manera:
# 
# - Ubicación por defecto en Google Colabs 
#   - En la pestaña de la izquierda que contiene los ícono de lupa, corchetes y carpeta, abrir la carpeta
#   - El archivo debe aparecer allí. Si se muestra una estructura de directorios, el archivo está en la carpeta llamada "*content*"
# 
# - Ubicación en Google Drive
#   - Es necesario "[montar el *drive*](https://colab.research.google.com/drive/1bP_e4pVvTUto_ZxYM9vE63cMaAiwJxRG?usp=sharing)" para especificar la ubicación del Google Drive del usuario
#   - Una vez montado, se debe especificar una dirección  hacia la carpeta dentro del *drive* donde se quiere guardar el archivo

# In[40]:


# Guarda los datos escogidos en el archivo especificado
#     np.savetxt ( [Dónde-->archivo], [Qué-->Arreglo], [Cómo-->Formato])    

nombre_archivo = 'resultado_funcion.txt'
encabezado = 'x    y = cos(x^2)'
np.savetxt(nombre_archivo, datos_dos_columnas, delimiter='\t', header=encabezado)


# **1.4.3 Genera una gráfica y la guarda a un archivo**
# 
# 

# In[41]:


import matplotlib.pyplot as plt

# Ajusta el tamaño de la figura (ancho y alto)
plt.figure(figsize = (6,3.4)) 
plt.style.use('default')
#plt.style.use ('seaborn-poster')

# Grafica los arreglos de datos con los atributos de línea
plt.plot(datos_x, datos_y, color='green', linestyle = 'dashed')
# Atributos de la gráfica
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función f(x) = cos(x^2)')
plt.grid()

# Guarda la gráfica un archivo
plt.savefig('grafico_funcion.png', dpi=150)
plt.savefig('grafico_funcion.pdf', dpi=150)

# Muestra el gráfico
plt.show()


# ---
# ---
# ###1.5  Ejercicio para entregar 

# 
# **Ecuación de Arrhenius:**
# 
# Es de conocimiento común que las reacciones químicas ocurren más rápidamente a temperaturas más altas; por ejemplo, la leche se pone agria mucho más rápidamente si se almacena a temperatura ambiente en lugar de en un refrigerador.  
# 
# La [velocidad de reacción](https://en.wikipedia.org/wiki/Reaction_rate) $k$ permite estimar la cantidad de sustancia que se transforma por unidad de tiempo en una reacción química determinada. La ecuación de Arrhenius suministra una relación matemática entre la velocidad de reacción $k$ y la temperatura $T$. Este modelo se basa en la idea de que a  medida que aumenta la temperatura, las moléculas se mueven más rápido y chocan con mayor intensidad, aumentando la probabilidad de que ocurra una reacción química.
# 
# De acuerdo con esta ecuación 
# $$k = A\, \exp\left( -\frac{E_a}{R\,T}\right)$$
# donde 
# - $k$ es la velocidad de reacción ($\text{s}^{-1}$)
# - T es la temperatura absoluta ($\text{K}$)
# - $A$ es un factor constante ($\text{s}^{-1}$)
# - $E_a$ es la energía de activación de la reacción ($\text{J}\cdot\text{mol}^{-1}$)
# - $R$ es la constante universal de los gases ($\text{J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$).

# **Problema:**
# 
# 1. Defina una función que permita evaluar la velocidad de reacción $k$ tomando como argumentos de entrada $T$, $A$, $E_a$, y $R$
# 
# 2. Usando arreglos adecuados, evalúe la tasa de reacción para el rango de temperatura 
# $-20~^\circ\text{C} \le T \le 100~^\circ\text{C}$ de una reacción caracterizada por una energía de activación $E_a = 52.0~\text{kJ}\cdot\text{mol}^{−1}$ y una constante $A = 1.00~\text{s}^{-1}$. 
# 
#  Nota: Recuerde que $T [\text{K}] = T [^\circ\text{C}] + 273.15$ $~$y$~$ $R = 8.31~\text{J}\cdot\text{K}^{−1}\cdot\text{mol}^{−1}$
#  
# 3. Almacene los arreglos de datos obtenidos en un archivo de texto de tres columnas que contenga (i) la temperatura en grados Celsius, (ii) la temperatura en Kelvin y (iii) la velocidad de reacción evaluada. El nombre del archivo debe ser "velocidad_de_reaccion.dat" 
# 
# 4. Grafique la curva $k$ vs $T$ en el rango solicitado  y guardela en el archivo El nombre del archivo debe ser "velocidad_de_reaccion.png" 

# **Solución**:

# 1. Define de la función correspondiente a  la ecuación de Arrhenius

# In[23]:


# Importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
# Definir la ecuación de Arrhenius
# en términos de los argumentos 
def Arrhenius(a,b,c,x):
  expo = -((b)/(c*x))
  ecua = a*np.exp(expo)
  return ecua


# 2. Evalúa los arreglos necesarios psra generar los datos necesarios

# In[24]:


# Definir las variables necesarias
a = 1.00
ea = 52000.0
r = 8.31
# Definir el arreglo de temperatura
tempc = np.linspace(-20,100,121)
tempk = tempc+273.15

# Evaluar el arreglo correspondiente 
# a la velocidad de reacción
valor_y = Arrhenius(a,ea,r,tempk)


# 3. Guarda los datos solicitados en un archivo de texto

# In[42]:


# Preparar  un arreglo con los datos en columnas para 
# ser almacenados 
datos = np.column_stack((tempc,tempk,valor_y))
# Guardar los datos escogidos en el archivo especificado
np.savetxt('velocidad_de_reaccion.dat',datos,delimiter = '\t')


# 4. Grafica los datos solicitados y guarda la gráfica en un archivo

# In[47]:


# Graficar los datos solicitados y guardar la gráfica
plt.figure(figsize = (7,4)) 
plt.style.use('default')
# Graficar datos
plt.plot(tempk,valor_y,ls='--',color='red')
# Atributos de la gráfica
plt.title('Ecuación de Arrhenius')
plt.xlabel('Temperatura en °K')
plt.ylabel('Velocidad de reacción')
plt.grid()
# Guardar la gráfica
plt.savefig('velocidad_de_reaccion.png')
# Mostrar la gráfica
plt.show()

