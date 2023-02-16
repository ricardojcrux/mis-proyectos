#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 1 (20/09/2022) 

# ---
# ## 1. Elementos básicos de programación  
# 
# Describa brevemente cada uno de los siguientes conceptos
# * Algoritmo
# * Diagrama de flujo
# * Sistema operativo
# * Programa informático
# * Lenguaje de programación
# * Entorno de desarrollo

# ---
# ## 2. Cuadernos de Colab (*Notebooks*)
# 
# Los *notebooks* de Colab permiten mezclar en un mismo documento código ejecutable de Python con texto enriquecido (formatos, ecuaciones, imágenes, etc).
# - Archivos de extensión **.ipynb**
# 
# **Ventajas**
# - Suaviza la curva de aprendizaje
# - Almacenado en Google Drive
# - Trabajo colaborativo
# 
# **Desventajas**
# - Se requiere conexión a internet
# - Se pueden perder datos al cerrar la máquina virtual
# - Limitado a Python
# 
# ### 2.1 Celdas
# 
# Cada cuaderno se compone de celdas que pueden contener  *código* o *texto enriquecido*
# 

# 2.1.1 Celda con texto enriquecido: 
# 
# Esta puede  contener
# - texto plano
# - texto con formato: *itálica*, **negrita**, <font color='red'> color </font>
# - símbolos: $\alpha$, $\beta$, $\gamma$ 
# - ecuaciones: $a\,x + b = 0$  ($\LaTeX$)
# - enlaces: [Campus Vitual](https://campusvirtual.univalle.edu.co/moodle/)
# - etc

# 2.1.2 Celda con código ejecutable
# 
# Contienen comandos del lenguaje python, así como comentarios que deben iniciar con el símbolo "numeral" $(\texttt{#})$

# In[ ]:


# La ejecución de esta celda permite mostrar
# el resultado de las operaciones 

print(1 + 1)

a = 5 
b = 3
c = a * b
print(c)


# ---
# ## 3. Elementos básicos de python

# ### 3.1 Variables y asignaciones
# 
# - Las variables puede verse como un **nombre** dado en referencia a un **objeto/valor**
# - este nombre puede contener carácteres alfanuméricos (a-z, A-Z, 0-9) y el guión bajo (por ejemplo: $\texttt{numero_documento}$)
# - No se pueden usar ciertas palabras reservadas
#   > $\texttt{and}$, $\texttt{as}$, $\texttt{assert}$, $\texttt{break}$, $\texttt{class}$, $\texttt{continue}$, $\texttt{def}$, $\texttt{del}$, $\texttt{elif}$, $\texttt{else}$, $\texttt{except}$,  $\texttt{exec}$, $\texttt{finally}$, $\texttt{for}$, $\texttt{from}$, $\texttt{global}$, $\texttt{if}$, $\texttt{import}$, $\texttt{in}$, $\texttt{is}$, $\texttt{lambda}$, $\texttt{not}$, $\texttt{or}$,   $\texttt{pass}$, $\texttt{print}$, $\texttt{raise}$, $\texttt{return}$, $\texttt{try}$, $\texttt{while}$, $\texttt{with}$, $\texttt{yield}$ 
# - Las buenas prácticas indican que los nombres de variables deben:
#   * empezar con minúscula 
#   * ser autoexplicativos
# - A una variable se le asigna un valor a través del operador "$\texttt{=}$"  

# 3.1.1 Tipos de variables
# 
# 

# In[ ]:


# Ejemplos de tipos de variable

type('Pedro') # cadena de caracteres (texto)


# In[ ]:


type(2) # número entero


# In[ ]:


type(2.0) # Número real (punto flotante)


# In[ ]:


type( True ) # Variable booleana


# In[ ]:


type( [1, 2 , 3.14, True, 'Pedro'] )  # Lista


# 3.1.2 Asignaciones y operaciones

# In[ ]:


# Asignación de variables

a = 3 
b = 4.0

x = True
y = False


# In[ ]:


# Operaciones aritméticas

c1 = a + b
print(' c1 = ', c1)
c2 = a - b
print(' c2 = ', c2)
c3 = a * b
print(' c3 = ', c3)
c4 = a / b
print(' c4 = ', c4)
c5 = b ** a
print(' c5 = ', c5)


# In[ ]:


# Operaciones lógicas

print(b != a)  
print(a == b)
print(a > b)
print(b > a)

print('(x == y) =', x == y)
print('(x and y) =', x and y)
print('(x or y) =', x or y)
print('(not y) =', not y)


# In[ ]:


# Listas
# En python, una lista es un tipo contenedor empleado
# para almacenar conjuntos de elementos relacionados 
# del mismo tipo o de tipos distintos

mi_lista1 = [a, b, x]
mi_lista2 = [1, 2, 3]  

print('mi_lista1 = ', mi_lista1)
print('mi_lista2 = ', mi_lista2)

# Concatenación de listas
mi_lista3 = mi_lista1 + mi_lista2
print('mi_lista3 = ', mi_lista3)

# Lista vacia

mi_lista_vacia = []
print('')
print('mi_lista_vacia = ', mi_lista_vacia)


# 3.1.3 Estructura '$\texttt{if - else}$'
# 

# In[ ]:


# Este programa determina si un número dado 
# es positivo o no

# Entrada estándar
entrada = float(input('* Escriba un número: '))

# Estructura if-else
if ( entrada > 0 ): # Condición            	                        
    # La condición es verdadera
    resultado = 'el número ingresado es positivo'  	
else:
    # La condición es falsa
    resultado = 'el número ingresado NO es positivo' 

# Salida estándar
print('* Resultado: ', resultado )


# ## 3.2 Ejercicio propuesto
# 
# Considere la  ecuación lineal $a x + b = 0$ para valores reales dados de los coeficientes $a\ne 0$ y $b$. Proponga un programa para mostrar la solución de la ecuación únicamente cuando ésta sea positiva.    
#     

# In[3]:


# Este código muestra la solución de la 
# ecuación "a*x + b = 0", solo cuando es 
# positiva

a = float(input('Ingrese el valor a: '))
b = float(input('Ingrese el valor b: '))

tot = -b/a

if (tot > 0) :
  print('El resultado es: ',tot)
else:
  print('El resultado no es positivio')

