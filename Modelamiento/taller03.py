#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 3 (04/10/2022)

# ## 1. Elementos básicos de python
# 
# 
# 

# ---
# ---
# ### 1.1 Repaso
# 
# **1.1.1 Estructuras cíclicas $\texttt{for}$ y $\texttt{while}$**
# 
# - Describa la brevemente las funciones $\texttt{len()}$ y $\texttt{range()}$, y su relación con procesos cíclicos
# - ¿Cuáles son las características de un ciclo $\texttt{for}$?
# - ¿Cuáles son las características de un ciclo $\texttt{while}$?
# - ¿Cuál es la función de la declaración $\texttt{break}$?
# 

# ---
# **Solución del problema propuesto en la última sesión -> Número primo**
# 
# *Problema:*
# 
# Realizar un programa que verifique si un número entero dado es o no un número primo. 
# 
# 1.   Esboze el algoritmo  para responder a la tarea planteada usando un ciclo $\texttt{while}$
# 2. Escriba y ejecute el código correspondiente
# 

# *Solución:*
# 1. Para responder al primer punto se puede considerar un algoritmo como el mostrado en este [diagrama de flujo](https://drive.google.com/file/d/1U2yNO457amLXu0L6f58JxWTRN2GEWsyb/view?usp=sharing)
# 2. La implementación en python de este algoritmo puede ser de la siguiente manera:

# In[2]:


# Este programa verifica si un número entero dado 
# es primo o no haciendo uso del ciclo while

# Ingresar numero natural para verificar si es o no primo
numero_prueba = 0
while numero_prueba < 2:
  numero_prueba = int(input('Ingrese un número entero mayor que 2:  ')) 

# Asignación de variables
es_primo = True     # Se supone que el número es primo
numero_divisor = 2  # Valor inicial de los divisores  

while (numero_divisor < numero_prueba): 
    # Verifica si "divisor" divide a "numero_prueba"    
    residuo = numero_prueba % numero_divisor   
    if (residuo == 0):                            
      # Si se cumple, "numero_prueba" no es primo
      es_primo = False  
      break    
    else: 
      # si el residuo no es cero, cambia el divisor 
      numero_divisor += 1 

# Escribe el resultado de la verificación        
if es_primo == True:            
  print('\n El número %i es primo' %numero_prueba)
else:            
  print('\n El número %i NO es primo' %numero_prueba)  


# ---
# **1.1.2 Problema propuesto -> Número primo**
# 
# Realizar un programa que verifique si un número entero dado es o no un número primo usando [el ciclo $\texttt{for}$](https://drive.google.com/file/d/1EPPb048QIfHy9oU1JYayD_gIQ1SyPT9F/view?usp=sharing)

# In[ ]:


# Este programa verifica si un número entero dado 
# es primo o no haciendo uso del ciclo for

# Ingresar numero natural para verificar si es o no primo


# Asignación de variables


# Ciclo sobre los posibles divisores
   

# Escribe el resultado de la verificación        
 


# ---
# ---
# ### 1.2 Funciones

# **1.2.1 Definición y uso**
# 
# En Python, una función es un grupo de declaraciones relacionadas que realizan una tarea específica.
# - variables de entrada (argumentos) y variables de salida (resultado)
# - permiten dividir un programa en partes más pequeñas
# - hacen que un programa sea más organizado y manejable
# - evitan repetir trabajos previos (código reutilizable)
# - pueden ser predefinidas o definas por el usuario
# 
# 

# 
# *- Funciones predefinidas:* Por ejemplo, $\texttt{len()}$ es una función que toma como entrada una lista y como resultado arroja el número de elementos de dicha lista;  $\texttt{range()}$ es una función que arroja una secuencia de enteros especificados por los argumentos introducidos (inicio, fin, paso)
# 
# - Funciones de la librería estándar
# - Funciones de librerías especializadas
# 
# *- Funciones definidas por el usuario:* Ofrecen la posibilidad de crear tareas que se adapten a las  necesidades propias. Para crear una función se debe considerar la siguiente sintaxis:
# ```
#  def nombre_funcion(argumento_1, argumento_2, ...):
#     declaracion_1
#     declaracion_2
#     ....
#     return expresion_salida
# ```
# 
# 

# ---
# **1.2.2 Ejemplos**
# 

# Ejemplo 1: Definir la función $f(x) = x^2 + x + 1$

# In[3]:


# Define la función f(x) = x^2 + x + 1
#   - Toma UN argumento 
#   - Retorna UNA salida

def mi_funcion(x):   
  # x es el argumento de la función
  # fx es el resultado de evaluar la función
  fx = x**2 + x + 1  
  return fx   


# In[4]:


# Llama y evalúa la función definida para 
# distintos valores del argumento  

print('El resultado de evaluar f(12) es', mi_funcion(12))
print('El resultado de evaluar f(1)  es', mi_funcion(1))
print('El resultado de evaluar f(9)  es', mi_funcion(9)) 


# Ejemplo 2: Definir la función $f(x,y) = x^2 + y^2$

# In[5]:


# Define la función f(x,y) = x^2 + y^2
#   - Toma DOS argumentos 
#   - Retorna UNA salida

def funcion_dos_variables(x,y):   
  fxy = x**2 + y**2  
  return fxy 


# In[6]:


# Llama y evalúa la función definida para 
# distintos valores de los argumentos  

print('El valor de f(1,2) es',  funcion_dos_variables(1,2) )
print('El valor de f(0,4) es',  funcion_dos_variables(0,4) )
print('El valor de f(-1,3) es',  funcion_dos_variables(-1,3) )


# Ejemplo 3: Definir una función SIN argumentos
# 
#  
# 
# 

# In[7]:


# Define una función SIN argumentos

def funcion_saludar( ):
  return '¡Hola, hola!'

# Evalua la función con solo llamarla

print( funcion_saludar() )


# Ejemplo 4: Definir la función 
# $$f(x) = \begin{cases}
# -x & x \le -2 \\
# \quad 2 & -2 < x < 2 \\
# \quad x & 2 \le x
# \end{cases}$$
# 

# In[8]:


def mi_funcion_condicional(x):           
    if (x<=-2):
      y = -x                
    elif (-2< x and x<2):
      y = 2
    else:
      y = x       
    return y   


# In[9]:


# Llama y evalúa la función definida para 
# distintos valores del argumento

for indice in range(-4,5):
  print( 'x, f(x) =', indice, ',', mi_funcion_condicional(indice) )


# Ejemplo 5: Definir funciones que nos ayuden a convertir temperaturas en grados Fahrenheit a grados Celsius y viceversa

# In[10]:


# Definición de la función que convierte 
# la temperatura de °C a °F
#   temp_celsius    = argumento
#   temp_fahrenheit = salida (resultado)
def celsius_a_fahrenheit(temp_celsius):
  temp_fahrenheit = (5/9)*temp_celsius + 32
  return temp_fahrenheit

# Definición de la función que convierte 
# la temperatura de °F a °C
#   temp_fahrenheit = argumento
#   temp_celsius    = salida (resultado)
def fahrenheit_a_celsius(temp_fahrenheit):
  temp_celsius = (9/5)*(temp_fahrenheit-32)
  return temp_celsius


# In[11]:


# Programa que usa (llama/invoca) las 
# funciones definidas por el usuario
#
# Uso de la función °C -> °F
T_en_C = 22
T_en_F = celsius_a_fahrenheit(T_en_C)
print('\n Función °C -> °F: ', T_en_C,'°C = ', T_en_F,'°F')

# Uso de la función °F -> °C
T_en_F = 34
T_en_C = fahrenheit_a_celsius(T_en_F)
print('\n Función °F -> °C: ', T_en_F,'°F = ', T_en_C,'°C')


# ---
# ---
# ### 1.3 Visualización de datos
# 
# 1.3.1 Librerías y módulos
# 
# - ¿Qué es una [librería](https://immune.institute/librerias-python-que-son/)?
#   - conjunto de archivos (códigos y datos) que se utiliza para desarrollar software
#   - tiene como fin ser utilizada por otros programas de forma autónoma  
#   - *matplotlib*, *numpy*, *scipy*, *pandas*, *TensorFlow*, *scikit-learn*, ...
#   - se importa usando el comando $\texttt{import}$
#   ```
#   import NombreLibreria as AliasLibreria
#   ```
# 
# - ¿Qué es un [módulo](https://docs.python.org/es/3/tutorial/modules.html)? 
#   - es un archivo particular que contiene un conjunto de funcionalidades específicas
#   - puede contener tanto declaraciones ejecutables como definiciones de funciones
#   - es un archivo importable
#   ```
#   import NombreLibreria.NombreModulo as AliasModulo
#   ```
# 
# 
# 
# 
# 

# ---
# 1.3.2 Librería $\texttt{matplotlib}$ y el módulo $\texttt{pyplot}$

# - **Librería $\texttt{matplotlib}$:** 
#   - permite crear visualizaciones estáticas, animadas e interactivas en python (https://matplotlib.org/)
#   - multiplataforma 
#   - puede usadarse desde scripts o desde la consola   (terminal) de python
#   - se puede exportar gráficas a diferentes formatos de imagen 
#   - alta calidad $\to$ inclusión en documentos de carácter académico o científico
# 
#     <font size=1> Imagen tomada de: https://stackoverflow.com/questions/915940/python-plotting-libraries </font> 
# 
#     <img src='https://i.stack.imgur.com/TEO2z.jpg' width="500">
# 
# - **Módulo $\texttt{pyplot}$:** 
#   - colección de funciones que "obliga" a $\texttt{matplotlib}$ a trabajar como MATLAB
#   - cada función de $\texttt{pyplot}$ realiza un cambio o agrega un atributo  a la figura 
#     - crea una figura
#     - crea un área de trazado en la figura
#     - crea líneas en el área de trazado
#     - asigna un color específico a las líneas
#     - ubica texto en una región específica de la figura
#     - etc

# 
# 1.3.2 Ejemplo de uso del módulo $\texttt{matplotlib.pyplot}$
# 
# Graficar la función $f(x) = ax^2+bx+c$ para los coeficientes $a=3$, $b=2$, $c=5$ y $x$ en el intervalo $[-5,5]$

# - Se crea la función que se quiere graficar

# In[12]:


# Define la función a graficar
def mi_funcion_cuadratica(x , a, b , c):    
    # x es el argumentos
    # a, b, c son los parámetros
    y = a*x**2 + b*x + c      
    return y 


# - Se generan los datos a graficar; en este caso se realiza a través del uso de listas
# 
# 

# In[13]:


# Define la lista de datos de entrada (eje x)
xmin = -5
xmax =  5
datos_X = list( range(xmin , xmax+1) )

# Define los valores de los coeficientes
a = 3 
b = 2
c = 5

# Evalua la función para cada valor de x (eje y)
datos_Y = []
for x in datos_X:
  y = mi_funcion_cuadratica(x , a, b , c)
  # Agrega el valor de y a la lista
  datos_Y += [y]

# Define una lista con todos los datos
datos_totales = [ datos_X , datos_Y ]

# Imprime los datos en la pantalla
print('Datos totales = ', datos_totales, '\n')


# - Se realiza la gráfica; requiere que se importe el módulo $\texttt{pyplot}$

# In[14]:


# Importa el módulo "pyplot" de la librería "matplotlib" 
# con el alias de "plt", con lo cual es posible crear
# gráficas de datos en 2D (gráficas xy)
import matplotlib.pyplot as plt

# Se introduce la secuencia de funciones de pyplot
# con las características de la gráfica

# Grafica las dos listas de valores
plt.plot(datos_X, datos_Y, '*-')

# Agrega nombres a los ejes (IMPORTANTE)
plt.xlabel('x [unidades]')
plt.ylabel('y [unidades]')

# Agrega un título al gráfico
plt.title('Gráfico de y =' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c) )    
          
# Agrega un mallado a la gráfica
plt.grid()

# Muestra el gráfico resultante
plt.show()


# ---
# **1.3.3 Problema propuesto (entregable) --> Temperatura vs tiempo**
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
# 1. Escriba un programa que permita evaluar la temperatura $T$ para cualquier instante $t$ en el intervalo de tiempo indicado
# 2. (opcional) ¿Puede explicar las razones físicas de dicho comportamiento?

# In[44]:


# Sección del programa para
# definir la función a graficar
def T(t):
  if (0<=t<10):
    z = 2*(t-10)
  elif(10<=t<20):
    z = 0
  elif(20<=t<35):
    z = (20/3)*(t-20)
  elif(35<=t<=50):
    z = 100
  return z 


# In[45]:


# Sección del programa empleada para
# graficar los datos solicitados
import matplotlib.pyplot as plt
# Define la lista del argumento
x = list(range(51))
# Evalúa la lista de la función
y = []
for i in x:
  num = T(i)
  y += [num]
# Grafica las listas de datos
plt.figure(figsize=(10,7))
plt.plot(x,y,'Purple')
plt.title('Gráfica de Temperatura vs Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura')
plt.grid()
plt.show()

