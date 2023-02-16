#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 5 (18/10/2022)

# ---
# ---
# ## 1. Elementos básicos de python
# 

# 
# - *Sintaxis*: comandos, identación (sangría)
# - *Variables*: variables lógicas, listas (indexación, concatenación)
# - *Estructuras condicionales*: $\texttt{if}\dots\texttt{elif}\dots\texttt{else}$
# - *Estructuras cíclicas*: $\texttt{for}$, $\texttt{while}$ 
# - *Funciones*: definición y llamado
# - *Gráficos*: módulo gráfico $\texttt{matplotlib.pyplot}$
# - *Arreglos*: librería numpy, definición, operaciones y funciones con arreglos
# - Almacenar datos y gráficas a archivos: formato CSV, $\texttt{np.savetxt()}$, $\texttt{plt.savefig()}$ 

# ---
# ---
# ###1.1 Repaso última sesión
# 
# **1.1.1 La librería NumPy**
# 
# - En python, ¿qué es un NumPy?
# - En python, ¿qué es un arreglo?
# - ¿Cuáles son los elementos mínimos necesarios para almacenar en un archivo de texto los datos contenidos en uno o varios arreglos?
# 
# **1.1.2 Uso de los arreglos para graficar y almacenar datos**
# 
# **Ejercicio anterior: Ecuación de Arrhenius**
# 
# > La ecuación de Arrhenius suministra una relación matemática entre la velocidad de reacción $k$ y la temperatura $T$ dada por la expresión: 
# $$k = A\, \exp\left( -\frac{E_a}{R\,T}\right),$$
# donde 
# - $k$ es la velocidad de reacción ($\text{s}^{-1}$)
# - T es la temperatura absoluta ($\text{K}$)
# - $A$ es un factor constante ($\text{s}^{-1}$)
# - $E_a$ es la energía de activación de la reacción ($\text{J}\cdot\text{mol}^{-1}$)
# - $R$ es la constante universal de los gases ($\text{J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$).

# - **Problema:**
# 
# > 1. Defina una función que permita evaluar la velocidad de reacción $k$ tomando como argumentos de entrada $T$, $A$, $E_a$, y $R$
# 
# > 2. Usando arreglos adecuados, evalúe la tasa de reacción para el rango de temperatura 
# $-20~^\circ\text{C} \le T \le 100~^\circ\text{C}$ de una reacción caracterizada por una energía de activación $E_a = 52.0~\text{kJ}\cdot\text{mol}^{−1}$ y una constante $A = 1.00~\text{s}^{-1}$. \\
# Nota: Recuerde que $T [\text{K}] = T [^\circ\text{C}] + 273.15$ $~$y$~$ $R = 8.31~\text{J}\cdot\text{K}^{−1}\cdot\text{mol}^{−1}$
#  
# > 3. Almacene los arreglos de datos obtenidos en un archivo de texto de tres columnas que contenga (i) la temperatura en grados Celsius, (ii) la temperatura en Kelvin y (iii) la velocidad de reacción evaluada. El nombre del archivo debe ser "velocidad_de_reaccion.dat" 
# 
# > 4. Grafique la curva $k$ vs $T$ en el rango solicitado  y guardela en el archivo "velocidad_de_reaccion.png" 

# - **Solución**:

# In[ ]:


# PRIMER PUNTO: DEFINICION DE LA ECUACION DE ARRHENIUS

# Importa las librerías necesarias 
import numpy as np
import matplotlib.pyplot as plt

# Define la ecuación de Arrhenius a través de una función
def velocidad_de_reaccion(Temp, Acoef, Eact, Rgas):  
  # Los valores de los argumentos deben introducirse 
  # en las unidades adecuadas
  vel_reac_k = Acoef * np.exp( - Eact / (Rgas*Temp) )
  return vel_reac_k 


# In[ ]:


# SEGUNDO PUNTO: EVALUACIÓN DE LA TASA DE REACCIÓN

# Parámetros (en unidades adecuadas)
Ea = 52.0 * 10**3 # J/mol
A  = 1.00         # 1/s 
R  = 8.31         # J/(K*mol)

# Arreglo de temperaturas en °C y en K
T_en_C = np.linspace(20,100,31)
T_en_K = T_en_C + 273.15

# Evalúa la velocidad de reacción para los
# parámetros dados
k_reaccion = velocidad_de_reaccion(T_en_K, A, Ea, R)


# In[ ]:


# TERCER PUNTO: ALMACENAMIENTO DE LOS RESULTADOS NUMÉRICOS

# Prepara un arreglo con los datos en columnas para 
# ser almacenado
datos_tres_columnas = np.column_stack( ( T_en_C, T_en_K, k_reaccion ) )

# Guarda los datos escogidos en el archivo especificado
nombre_archivo = 'velocidad_de_reaccion.dat'
encabezado = '     T(°C)        T(K)          k(1/s)'
formato_numeros = '%12.3f %12.3f %18.6e'
np.savetxt(nombre_archivo, datos_tres_columnas, delimiter='\t', header = encabezado, fmt = formato_numeros)


# In[ ]:


# CUARTO PUNTO: VISUALIZACIÓN DE LOS DATOS Y ALMACENAMIENTO DEL GRÁFICO RESULTANTE

# Estilo de la gráfica
plt.figure(figsize = (5,2.8)) 
plt.style.use ('default')
# Grafica los datos
plt.plot(T_en_C, k_reaccion, marker='o', linestyle = 'dotted')
# Atributos de la gráfica
plt.xlabel('Temperatura  [°C]')
plt.ylabel('Velocidad de reacción  [1/s]')
plt.title('Ecuación de Arrhenius')
plt.grid()
# Guarda y muestra la figura
plt.savefig('velocidad_de_reaccion.png', dpi=150)
plt.show()


# In[ ]:


# Este comnado permite ver lso formatos a los
# cuales se puede exportar una gráfica
plt.gcf().canvas.get_supported_filetypes()


# ---
# ---
# ###1.2 Lectura de datos
# 
# - Al realizar análisis de datos, frecuentemente es necesario "leerlos" a partir de archivos en distintos  formatos. La librería *NumPy* permite leer [archivos CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas)  fácilmente. 
# 
# - Un archivo  CSV es un archivo texto plano sin formato que facilita la manipulación de datos y es más fácil de importar a una hoja de cálculo o base de datos  

# **1.2.1 Importar un arreglo a partir de un archivo CVS**
# 
# - *NumPy* proporciona varias funciones para crear arreglos a partir de datos tabulados
# 
# - Una de ellas es  $\texttt{loadtxt()}$ 
# 
# - Esta función ejecuta dos bucles principales: 
#    - 1ro: convierte cada línea del archivo en una cadena de caracteres
#    - 2do: convierte cada cadena al tipo de datos apropiado
# 
# - Sintaxis:
#   ```
#   arreglo_importado = np.loadtxt(nombre_archivo, delimitador)
#   ```
#   con
#   - nombre_archivo = cadena de caracteres 
#   - delimitador = cadena de caracteres; los más comunes son '\t' (tabulación) y ' , ' (coma) 

# **Ejemplo lectura de datos:** Realizar la gráfica de $y=\cos(x^2)$ vs $x$ a partir de los datos almacenados  en el archivo "[resultado_funcion.dat](https://drive.google.com/drive/folders/1PP-0T_A9A1BdJkZqLnkzLDNGcdB9K5Fc?usp=sharing)"
# 
# > *Nota*: Para importar los datos es necesario que el archivo esté ubicado en la carpeta de trabajo de Colabs. Para ello se debe:
#   - Descargar el archivo de Google Drive al PC
#   - Subir el archivo al directorio de trabajo (ícono de carpeta en la barra de la izquierda)  
# 

# In[ ]:


# Los siguientes comandos de linux permiten 
# chequear la estructura de nuestros archivos

# El comando "ls" permite listar las carpetas y 
# los archivos guardados en la carpeta de trabajo
get_ipython().system(' ls')


# In[ ]:


# El comando "head" permite ver las primeras  
# líneas de un archivo de texto
# En este caso la permite ver las cinco 
# primeras líneas con la opción "-n5"
get_ipython().system(' head -n5 resultado_funcion.dat')


# In[ ]:


# Importa las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np

# Recupera los datos del archivo a un arreglo 2D
datos_recuperados = np.loadtxt('resultado_funcion.dat')

# Muestra las primeras filas del arreglo de datos recuperados
print('Los datos recuperados son:\n\n', datos_recuperados[0:6,:],'\n ...') 


# In[ ]:


# Crea arreglos para las distintas columnas
# Nota: El encabezameinto se descarta automaticamente
arreglo_x = datos_recuperados[:,0] # La primera columna completa
arreglo_y = datos_recuperados[:,1] # La segunda columna completa

# Graficar los datos recuperados
plt.figure(figsize = (5,2.8)) 
plt.style.use('default')

plt.plot(arreglo_x, arreglo_y , marker='o' , linestyle=':')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x)=cos(x²)')
plt.grid()

plt.show() 


# ---
# ---
# 
# ## 2. Relaciones de proporcionalidad
# 
# ### 2.1 Definición
# 
# - La proporcionalidad entre dos magnitudes es la circunstancia en la que éstas mantienen entre sí una razón o cociente constante
# - En otras palabras, [dos variables $x$ e $y$ son proporcionales](https://drive.google.com/file/d/1LMGmoUPxxCLEffbq9gGMnl94umG44hRZ/view?usp=sharing) si un cambio en $x$ corresponde con una variación en $y$, siempre en la misma proporción
#   - Una relación de proporcionalidad directa ($y\propto x$) implica que
#     - $\dfrac{y}{x} = \text{constante}$ 
#   - Una relación de proporcionalidad inversa ($y\propto 1/x$) implica que
#     - $y \cdot x = \text{constante}$ 
# 
# ---
# ### 2.2 Ejemplo: Ecuación de los gases ideales
# 
# - La ecuación de estado de un gas ideal, la cual describe la relación entre la presión absoluta $P$, el volumen $V$, la temperatura absoluta $T$ y la cantidad de sustancia $n$ (en moles), está dada por la expresión
# $$ P = \frac{n\,R\,T}{V}, $$
# donde $R$ es la constante de los gases ideales.
# 
# - Se pueden obtener distintas relaciones de proporcionalidad entre las variables involucradas:
#   - Ley de Gay-Lussac: para $V$ y $n$ constantes (*procesos isocóricos*) se tiene
#   $$P = C_1\, T  $$
#   - Ley de Boyle: para $T$ y $n$ constantes (*procesos isotérmicos*) se tiene
#   $$P = \frac{C_2}{V}  $$
#   - Ley de Charles: para $P$ y $n$ constantes (*procesos isobáricos*) se tiene
#   $$V = C_3\,T  $$

# ---
# ---
# ---
# ###2.3  Ejercicio para entregar 
# 
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

# - **Solución primer punto: importar los datos**

# In[1]:


get_ipython().system(' head -n5 datos_proporcion.dat')


# In[8]:


# Importar las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np

# Recuperar los datos del archivo 
datos = np.loadtxt('datos_proporcion.dat')
datos_x = datos[:,0]
datos_y = datos[:,1]


# - **Solución segundo punto: graficar los datos y establecer el tipo de relación entre ellos**

# In[41]:


# Graficar los datos recuperados
plt.plot(datos_x,datos_y,'*-')
plt.title('Datos Proporcion')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# > ¿Qué tipo de relación existe entre las variables dadas? 
# 
# > *Respuesta*: Es una funcion de proporcionalidad inversa, ya que los datos decrecen segun lo señalado en la gráfica
#  
#     

# - **Solución tercer punto: estimar el valor de la constante $a$**
# 

# > Explique cómo se puede estimar el valor de la constante de proporcionalidad $a$
# 
# > *Respuesta*: Haremos un ciclo for para poder estimar el valor de la constante haciendo una sumatoria entre los valores de 'x' y 'y'
# 

# In[62]:


# Evaluación de la constante de proporcionalidad
number = len(datos_x)
lista = list(range(0,number))
cons = 0
for i in lista:
  a = datos_x[i]*datos_y[i]
  cons = cons + a
cons = cons/number
print(cons)


# - **Solución cuarto punto: comparar los datos con el modelo resultante**
# 

# In[63]:


# Graficar los datos recuperados
# y el modelo resultante
datos_y2 = cons/datos_x
plt.plot(datos_x,datos_y,'*-',label='Datos originales')
plt.plot(datos_x,datos_y2,'o-',label='Datos aproximados')
plt.title('Comparativa')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


# ---
# ---
# ---
# 
# ## 3. Regresión lineal por mínimos cuadrados
# 
# 
# ### 3.1 Definición
# 
# La [regresión lineal](https://www.imsl.com/blog/what-is-regression-model) es una técnica de modelado estadístico que se utiliza para describir una *variable de respuesta* en función de una o más *variables predictoras*. Puede ayudar a comprender y predecir el comportamiento de sistemas complejos o analizar datos experimentales, financieros, biológicos, etc.
# 
# - En una *regresión lineal simple* se utiliza un único predictor $X$, para describir una variable de respuesta $Y$,  lo cual se realiza a través de la ecuación general
# $$Y = \beta_0 + \beta_1\,X + \epsilon,$$
# en la que $\beta_0$ (*intercepto*) y $\beta_1$ (*pendiente*) son los parámetros del modelo y $\epsilon$ representa el término de error.
# 
# - Los parámetros del modelo, también llamados *coeficientes de regresión*, se deben calcular a partir del conjunto de datos u observaciones disponibles $\{(x_i,y_i),\,i=1,\dots,n\}$ y el término de error mide la diferencia entre las predicciones del modelo y las observaciones reales.
# 
# - La estimación de los parámetros $\beta_0$ y $\beta_1$ se realiza a través del *método de mínimos cuadrados*.

# ---
# ### 3.2 Método de mínimos cuadrados
# 
# * La idea del método es minimizar la suma de todas las diferencias cuadráticas entre los valores generados ($Y_i$) por la función modelo y los correspondientes valores de los datos reales ($y_i$). 
# 
# - En otras palabras el objetivo del método es  encontrar los valores de $\beta_0$ y $\beta_1$ tales que la función  
# $$E(\beta_0, \beta_1) = \sum_{i=1}^n\left[ y_i - Y_i \right]^2 = \sum_{i=1}^n\left[ y_i - (\beta_0 + \beta_1\,x_i)\right]^2$$ 
#  tenga el mínimo valor posible.
# 
# - Para evaluación los  parámetros a partir de los datos hay que minimizar $E(\beta_0, \beta_1)$
# 
# - Al realizar el proceso de minimización de la función $E(\beta_0, \beta_1)$ se obtiene:
# 
#   - Valor estimado del intercepto: 
#   
#   $$\beta_0  \equiv b = \frac{S_{xx}\cdot S_y  - S_{xy}\cdot S_x }{n\cdot S_ {xx} - S_x^2  } $$
# 
#    - Valor estimado de la pendiente:
#   $$\beta_1   \equiv m =  \frac{n\cdot S_{xy} - S_x\cdot S_y }{n\cdot S_{xx}- S_x^2}, \color{white}{........} $$
# 
# - En las expresiones anteriores  se han definido las siguientes sumatorias
#   $$ S_x = \sum_{i=1}^{n} x_i, \hspace{3ex}  
#   S_y =   \sum_{i=1}^{n} y_i, \hspace{3ex}
#   S_{xx} =   \sum_{i=1}^{n} x_i^2, \hspace{3ex}
#   S_{xy} = \sum_{i=1}^{n} x_i y_i, $$
# 
#   las cuales se calculan usando los datos disponibles $\{(x_i,y_i)\}$. 
# 
# 

# ---
# ### 3.3 Ejemplo
# 
# En la tabla se muestran algunas medidas de estatura y masa corporal que se tomaron a un determinado grupo de personas practicantes de baloncesto.
# 
#  Estatura | Peso
# --------|-----------
# (m)  | (kg)
# 1.55 |  51
# 1.57 |  50
# 1.62 |  55
# 1.68 |  52
# 1.75 |  60
# 1.75 |  68
# 1.81 |  78
# 1.83 |  91
# 1.87 |  84
# 1.89 |  81
# 1.90 |  90
# 1.92 | 105
# 1.95 |  95
# 1.95 |  99
# 1.99 | 100
# 2.02 | 101
# 
# **Problema**
# 
# - Determine una relación entre la estatura (*variable predictora*) y la masa corporal (*variable de respuesta*) para el grupo de personas seleccionadas. No olvide indicar las unidades de los parámetros del modelo ($\beta_0$ y $\beta_1$)
# - De acuerdo con la relación determinada, estime la masa corporal para una persona de estatura
#   - 1.40 m 
#   - 1.70 m 
#   - 2.10 m
# - El [índice de masa corporal](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal) $\text{(IMC)}$ es un indicador que ayuda a clasificar el peso de las personas en las siguientes categorías: *infrapeso* ($\text{IMC}< 19$), *peso normal* ($19<\text{IMC}<25$), *sobrepeso* ($25<\text{IMC}<30$) y *obesidad* ($30<\text{IMC}$). Este índice se evalúa según 
# 
#   $$\text{IMC} = \frac{\text{masa corporal [kg]}}{(\text{estatura [m])}^2}.$$
# 
#   Compare el  $\text{(IMC)}$ obtenido de los datos originales y el predicho por el modelo de regresión

# **Solución**

# > **1. Datos de entrada - Visualización**
# 
# >  Antes de empezar con un análisis de regresión es importante hacer un análisis exploratorio de los datos. En el caso de que se tenga la dependencia entre dos o tres variables, un gráfico de dispersión es apropiado para darse una primera idea de la relación entre ellas.

# In[ ]:


# Importar las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# Datos representados en la tabla (usando arreglos)
estatura      = np.array([1.55, 1.57, 1.62, 1.68, 1.75, 1.75,	1.81,	1.83,	1.87,	1.89,	1.90,	1.92,	1.95,	1.95,	1.99,	2.02])
masa_corporal = np.array([51,	50,	55,	52,	60,	68,	78,	91,	84,	81,	90,	105,	95,	99,	100,	101])

# Genera una gráfica "x vs y""
plt.figure(figsize = (5,2.8)) 
plt.style.use('default')            



# 
# > **2. Análisis de regresión simple ("Ajuste lineal")**
# 
# >  Se supone una relación lineal entre las variables:
#    $$\text{Masa corporal} = \beta_0 + \beta_1 \cdot \text{estatura}$$
# 
# >  La evaluación de los parámetros de la regresión ($\beta_0 = $ intercepto  y $\beta_1 = $pendiente) parte de la evaluación de las sumatorias $S_x$, $S_y$, $S_{xx}$ y $S_{xy}$ definidas arriba  en términos del conjunto de datos $\{(x_i,y_i),i=1,\dots,n\}$ 

# In[ ]:


# Evaluación de las sumatorias necesarias para 
# calcular los coeficientes de regresión

# Usando las funciones de numpy
numero_datos =  
suma_x  =  
suma_y  =  
suma_xx =  
suma_xy =  

# Los dos coeficientes tienen un denominador común
denominador =  


# In[ ]:


# Evaluación de beta0 (intercepto) y beta1 (pendiente)

beta0 =  
beta1 =  

print('Modelo: masa_corporal = beta0 + beta1*estatura \n')
print('Parámetro de regresión beta0 (intercepto) = %7.3f' % beta0, 'kg \n')
print('Parámetro de regresión beta1 (pendiente)  = %7.3f' % beta1, 'kg/m ')


# > **3. Comparación del modelo con las observaciones**

# In[ ]:


# Determinación de la predicción del modelo

# Para todos los x
masa_corporal_modelo =  

# Graficar el resultado de la regresión junto con los datos
plt.figure(figsize = (5,2.8)) 
plt.style.use('default')            
# Grafica los datos observados
plt.plot(estatura, masa_corporal,'o', label='Observaciones')
# Grafica el modelo obtenido por regresión lineal
plt.plot(estatura, masa_corporal_modelo, label='Modelo')

plt.xlabel('Estatura (m)') 
plt.ylabel('Masa corporal  (kg)')   
plt.legend(loc='lower right')
plt.grid()                               
plt.show()  


# > **4. Predicciones del modelo**
# 
# > El modelo obtenido permite realizar estimaciones para valores $x$ que no están en la tabla de datos originales

# In[ ]:


# Predicciones del modelo
# para valores de estatura dados

estatura_supuesta = 1.40 
masa_corporal_prevista = beta0 + beta1*estatura_supuesta
print('* Caso 1:')
print('        Estatura supuesta = %5.2f' % estatura_supuesta, ' m')
print('   Masa corporal predicha = %5.2f' % masa_corporal_prevista , 'kg\n')

estatura_supuesta = 1.70 
masa_corporal_prevista = beta0 + beta1*estatura_supuesta
print('* Caso 2:')
print('        Estatura supuesta = %5.2f' % estatura_supuesta, ' m')
print('   Masa corporal predicha = %5.2f' % masa_corporal_prevista , 'kg\n')

estatura_supuesta = 2.10 
masa_corporal_prevista = beta0 + beta1*estatura_supuesta
print('* Caso 3:')
print('        Estatura supuesta = %5.2f' % estatura_supuesta, ' m')
print('   Masa corporal predicha = %5.2f' % masa_corporal_prevista , 'kg\n')


# In[ ]:


# Predicciones del modelo
# para el IMC

IMC_datos  = masa_corporal / estatura**2
IMC_modelo = masa_corporal_modelo / estatura**2

# Graficar la predicción del modelo
plt.figure(figsize = (5,2.8)) 
plt.style.use('default')
plt.plot(estatura, IMC_datos, 'o:', label = 'Observaciones')
plt.plot(estatura, IMC_modelo, '-', label = 'Modelo')
plt.xlabel('Estatura (m)') 
plt.ylabel('IMC  (kg/m²)')   
plt.grid()
plt.legend()
plt.show()


# ---
# ### 3.4 Regresion lineal usando el módulo $\texttt{scipy.stats}$

# - El análisis de regresión es una tarea común por lo que los lenguajes de programación traen herramientas predeterminadas para realizarlo. En el caso de Python, la librería científica *SciPy* tiene métodos para éste y otros tipos de análisis relacionados
# 
# - [*SciPy* (*Scientific Python*)](https://scipy.org/) es una librería de computación científica que si bien está basada en *NumPy*, proporciona más funciones de utilidad para la solución de problemas de optimización, de análisis estadístico y de procesamiento de señales.
# 
# - El módulo $\texttt{scipy.stats}$ contiene una gran cantidad de herramientas relacionadas con distribuciones de probabilidad, estadísticas descriptivas, histogramas, funciones de correlación, pruebas estadísticas, regresión, etc...
# 
# - Sintaxis para importar las herramientas estadísticas
# ```
# import scipy.stats as stat 
# ```
# 
# 
# 
# 

# In[ ]:


get_ipython().system(' pip show scipy')


# In[ ]:


# Importar las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat

# Datos a ajustar (usando arreglos)
datos_x = np.array([1.5, 2.2, 3.0 ,4.0, 5.0, 6.0, 6.6])
datos_y = np.array([0.5, 2.5, 2.6 ,4.0, 3.5, 6.0, 5.5])

# Evalúa la regresion lineal con scipy
regresion_lineal = stat.linregress(datos_x, datos_y)

# Resultados del análisis (parámetros del modelo)
beta0 = regresion_lineal.intercept   # Intercepto
beta1 = regresion_lineal.slope       # Pendiente 

# Valores y estimados por el modelo
modelo_y =   beta0 + beta1*datos_x 

# Graficar el resultado de la regresión
plt.figure(figsize = (5,2.8)) 
plt.style.use('default')

plt.plot(datos_x, datos_y, 'o', label='datos')              # datos
plt.plot(datos_x, modelo_y, label='ajuste usando scipy')    # modelo de regresión

plt.xlabel('Variable x') 
plt.ylabel('Variable y')  
plt.legend()
plt.grid()       
    
plt.show()    


# In[ ]:




