#!/usr/bin/env python
# coding: utf-8

# # IMM - Taller No 2 (27/09/2020)

# ## 1. Elementos básicos de python
# 
# 
# 
# 

# ---
# ### 1.1 Repaso
# 
# **1.1.1 Estructura condicional $\texttt{if-else}$**
# 
# - ¿Qué es una variable booleana?
# - ¿Qué es una declaración lógica?
# - ¿Qué es un pseudo-código?
# - Describa brevemente la sintáxis y el propósito de la estructura condicional  $\texttt{if-else}$
# 

# In[ ]:


x = 0
if  (x >= 0):

  raiz = x**(1/2)
  print("LA raiz de x es = " , raiz  )

else:
  print(" No existe la raiz real de un numero negativo")


# **1.1.2 Estructura condicional $\texttt{if-elif-else}$**

# In[ ]:


dinero_disponible = float(input('¿Dinero disponible?'))





# In[ ]:


# Asignación de variables
dinero_disponible = float(input('¿Dinero disponible? '))
precio_taxi = 10000
precio_bus  = 2400

# Estructura de decisión 
# 'if-elif-else'
if (precio_taxi <= dinero_disponible):
  resultado = 'voy en taxi'
elif (precio_bus <= dinero_disponible):
  resultado = 'voy en bus'
else:
  resultado = 'voy caminando'

# Presentación del resultado  
print('... entonces', resultado)


# ---
# ---
# ### 1.2 Listas 
# 
# - Las listas son conjuntos ordenados de elementos (números, cadenas, booleanos, listas, etc). 
# - Las listas se delimitan por corchetes ($\texttt{[ ]}$) y los elementos se separan por comas.
# - Que las listas pueda contener diferentes tipos de objetos, es decir, que no requieran ser *homogéneas*, las convierte en una herramienta poderosa de Python.  
# - Las listas son mutables, es decir, sus elementos se  pueden modificar, se pueden añadir nuevos elementos, o se pueden remover elementos.

# In[ ]:


y = []

MiLista=[ 1,2,3,4]

for x in range( 0 , 10000 + 1):
  y += [x**2]

print("la lista de y es=" , y )



# In[ ]:


31%28




# **1.2.1 Elementos de una lista (indexación)**
# 

# In[ ]:


# Asignación de una variable tipo  lista
mi_lista = [1.53, 2, True, 'rojo',  [3, 5]]

# Indexación - Llamado a elementos de la lista
# NOTA: ¡en python el conteo inicia en cero!

print('* primer elemento de la lista:    ',  mi_lista[0] )
print('* tercer elemento de la lista:    ',  mi_lista[2] )
print('* último elemento de la lista:    ',  mi_lista[-1])
print('* penútimo elemento de la lista:  ',  mi_lista[-2])


# In[ ]:


# Otras listas
primera_lista = ['Juan','Pérez',  35, 1.70, 65, True]
segunda_lista = ['María','Rojas', 22, 1.82, 67, False]

print('* primera lista = ', primera_lista)
print('* segunda lista = ', segunda_lista)


# In[ ]:


# Listas a partir de elementos de otras listas
nombres = [primera_lista[0], segunda_lista[0]]
apellidos = [primera_lista[1], segunda_lista[1]]
print('* nombres = ', nombres)
print('* apellidos = ', apellidos)


# In[ ]:


# Concatenación de listas
tercera_lista = primera_lista + segunda_lista
print('* tercera lista = ', tercera_lista)


# In[ ]:


# Número de elementos de una lista
# La función "len()" arroja el número de elementos de una lista
numero_elementos = len(primera_lista)
print('* La lista ', primera_lista) 
print('* tiene', numero_elementos, 'elementos\n') 

numero_elementos = len(tercera_lista)
print('* La lista ', tercera_lista) 
print('* tiene', numero_elementos, 'elementos') 


# **1.2.2 Lista vacia**
# 
# En ocasiones es necesario definir variables del tipo lista sin elementos (listas vacias) para que puedan ser empleadas posteriormente en un programa
# 

# In[ ]:


# Lista vacia
mi_lista = []
print('* mi_lista = ', mi_lista, '(La lista está vacía)')
print('* una lista vacía tiene ', len(mi_lista), 'elementos\n')

# Agregar términos (1er método - básico)
mi_lista = mi_lista + [1] 
print('* mi_lista = ', mi_lista, '(La lista ya NO está vacía)')

# Agregar términos (2do método - rápido)
mi_lista += [2] 
print('* mi_lista = ', mi_lista, '(La lista ya NO está vacía)')

# Agregar términos (3er método - ".append()")
mi_lista.append(3) 
print('* mi_lista = ', mi_lista, '(La lista ya NO está vacía)')


# In[ ]:


# La "resta" de listas no está definida
print('Produce un error pues la "resta" de listas no está definida')
mi_lista = mi_lista - [2] 
print('mi_lista = ', mi_lista, '(La lista ya NO está vacía)')


# **1.2.3 Función $\texttt{len()}$**
# 
# - Esta función arroja el número de elementos en una lista

# In[ ]:


# Número de elementos de una lista

numero_elementos = len(primera_lista)
print('* La lista ', primera_lista) 
print('* tiene', numero_elementos, 'elementos\n') 

numero_elementos = len(mi_lista)
print('* La lista ', mi_lista) 
print('* tiene', numero_elementos, 'elementos') 


# **1.2.4 Función  $\texttt{range()}$**
# 
# - *Forma por defecto*: La función $\texttt{range}(N)$ arroja una secuencia de números que comienza en 0, se incrementa en 1 y termina en $N-1$.
# - *Forma general*: La función $\texttt{range}(N_{\text{ini}},N_{\text{fin}}, \text{paso})$ arroja una secuencia de números que comienza en $N_{\text{ini}}$, se incrementa en $\text{paso}$ y termina en el valor anterior a $N_{\text{fin}}$ que cumple con los incrementos.
# 

# In[ ]:


# Crear una lista desde 0 hasta 4

# Función range()
secuencia_range = range(5)
print('    Tipo de variable:', type(secuencia_range))
print('Valor de la variable:', secuencia_range, '\n')

# Convertir range() en una lista
secuencia_lista = list(range(5))
print('    Tipo de variable:', type(secuencia_lista))
print('Valor de la variable:', secuencia_lista, '\n')


# In[ ]:


# Crear la lista [2, 4, 6, 8, 10, 12]
# usando la función range()

Nini = 2
Nfin = 13
paso = 2
lista_pedida = list( range(Nini,Nfin,paso)  )

print('Lista pedida = ', lista_pedida, '\n')


# ---
# ---
# ### 1.3 Estructuras cíclicas  
# 
# - Los ciclos (bucles, *loops*) se encuentran entre los conceptos de programación más básicos y poderosos
# - Un ciclo es una instrucción que se repite hasta que se alcanza una condición específica
# - En una estructura cíclica, el ciclo hace una pregunta y si la respuesta requiere una acción, ésta se ejecuta

# **1.3.1 Ciclos $\texttt{for}$** 
# 
# - Los ciclos $\texttt{for}$ permiten ejecutar repetidamente un bloque de código para cada uno de los elementos pertenecientes a una secuencia (lista iterable)
# - Requiere de una *variable* o de un *índice* que permita recorrer los elementos especificados de la lista iterable
# - Sintaxis
# ```
#  for elemento in lista_iterable:
#      Bloque de instrucciones
#      a ejecutar para cada 
#      elemento 
# ```
# - El bloque de comandos después de la instrucción $\texttt{for}$ debe estar *indentado*

# 
# **Ejemplo:** Imprimir cada uno de los elementos de una lista dada

# In[ ]:


# Ejemplo del uso de un ciclo "for" para imprimir uno por uno 
# los elementos de una lista dada
 
lista_dada = ['Juan', 'Luisa', 'Mario', 'Lucía', 'Gabriela', 'Cristobal', 'José']


# In[ ]:


# Ciclo sobre cada elemento de la lista

print('* Ciclo "for" sobre los elementos de la lista:')

for elemento in lista_dada:          # Ciclo sobre cada elemento de la lista
  print('   Elemento = ', elemento)  # Imprime cada elemento de la lista


# In[ ]:


# Ciclo sobre los índices de la lista

print('* Ciclo "for" sobre los índices de la lista:')

for indice in range(len(lista_dada)):   # Ciclo sobre todos los índices de la lista
    print('   Elemento = ', lista_dada[indice])  # Imprime el elemento correspondiente al índice


# **1.3.2 Problema propuesto -> suma de 1 a 10**
# 
# - Escriba un programa que evalúe la suma de todos los números naturales comprendidos entre el 1 y el 10. 
# - Ayuda: el  [diagrama de flujo](https://drive.google.com/file/d/1fCslXWiJpjE_VGQSv6XoPXuSmbr6b_JK/view?usp=sharing) para resolver este problema usando el ciclo $\texttt{for}$ se discute en las Notas de Clase.
# 
# 

# In[ ]:


# Este programa muestra el resultado
# de sumar todos los números naturales 
# comprendidos entre 1 y 10

# Asignar y definir las variables necesarias
a = 0
lista = list(range(1,11))
# Realizar el proceso cíclico adecuado
for i in lista:
  a = a + i
# Mostrar el resultado  
print('La suma da como resultado ' + str(a))


# **1.3.4 Instrucción $\texttt{break}$**
# 
# - Esta *keyword* se utiliza para controlar el funcionamiento de un ciclo, más específicamente para interrumpirlo si determinada condición se satisface.

# In[ ]:


# Este programa imprime los elementos de una lista dada 
# hasta que uno de ellos es igual a un valor especificado
# previamente

gases_nobles = ['helio', 'neón', 'argón', 'kriptón', 'xenón', 'radón', 'oganesón']

for elemento in gases_nobles:
  print('Elemento = ', elemento)
  if (elemento == 'kriptón'):
    break


# In[ ]:


# El orden de las instrucciones es importante
# El resultado de este ciclo es distinto al 
# del anterior

gases_nobles = ['helio', 'neón', 'argón', 'kriptón', 'xenón', 'radón', 'oganesón']

for elemento in gases_nobles:
  if (elemento == 'kriptón'):
    break
  print('Elemento = ', elemento)


# **1.3.5 Ciclos $\texttt{while}$** 
# 
# - Los ciclos $\texttt{while}$ permiten ejecutar repetidamente un bloque de código mientras una condición predeterminada se cumpla 
# - Sintaxis
# ```
#   while condicion_dada:
#       Bloque de instrucciones
#       a ejecutar mientras la 
#       condición dada se cumple
# ```
# - El bloque de comandos después de la instrucción $\texttt{while}$ debe estar *indentado*

# **Ejemplo:** Solicitar un número hasta que el número ingresados sea positivo

# In[ ]:


# Este código continúa solicitando al usuario 
# el ingreso de un número real positivo hasta 
# que efectivamente se ingrese un número positivo

# Asignación de variables
numero_ingresado = -1.0

# Ciclo while
while numero_ingresado <= 0:
    numero_ingresado = float(input('Ingrese un número real positivo: '))

# Muestra el resultado
print('\n')
print('El número positivo ingresado es:', numero_ingresado)


# **Ejemplo:** Programa que arroja el resultado de sumar todos los números enteros positivos menores o iguales que 45 usando el ciclo $\texttt{while}$. El  [diagrama de flujo](https://drive.google.com/file/d/1-JpzA9N-cCqbzbm2_g_DTgydDeR32eCh/view?usp=sharing) para resolver este problema usando el ciclo $\texttt{while}$ se discute en las Notas de Clase.
# 

# In[ ]:


# Este programa muestra el resultado
# de sumar todos los números naturales 
# comprendidos entre 1 y 45

# Asignar y definir las variables necesarias
suma = 0 # guarda el resultado de la suma
contador = 0 # contador

# Realizar el proceso cíclico adecuado
while (contador <= 45):    
    suma += contador
    contador += 1 

# Mostrar el resultado  
print ('Suma_total = ', suma )


# **1.3.6 Problema propuesto -> Número primo**
# 
# Realizar un programa que verifique si un número entero dado es o no un número primo. 
# 
# 1.   Esboze el algoritmo  para responder a la tarea planetada usando un ciclo $\texttt{while}$
# 2. Escriba y ejecute el código correspondiente

# *Ayuda*: Un número $N>1$  es un número primo si
# \begin{equation}
# N\,\%\,n \ne 0,
# \end{equation}
# para $n = 2,3,\dots,N-1$, donde la operación **módulo** se define como
# \begin{equation}
# m\,\%\, n = \text{residuo de la división } (m\div n).
# \end{equation}

# **Parte 1: Algoritmo**
# 
# Escriba los pasos necesario para  para resolver el problema
# 
# 1. Ponemos un input para ingresar el numero.
# 2. Creamos una lista desde el numero 1 hasta el numero dado
# 3. Creamos un ciclo while para iterar cada numero
# 4. Con un if comprobamos que el residuo la division entre cada numero de la lista y el numero dado es 0
# 5. Con un elif mostramos que en caso que en ningun caso sea 0, confirmamos que el numero dado es primo
# 6. Imprimimos el mensaje confirmando o negando si el numero dado es primo o no

# **Parte 2: Implementación del algoritmo**

# In[11]:


# Este programa verifica si un número entero dado es primo
a=int(input('Escriba un número mayor que 2 ')) #Ingresamos un numero y lo volvemos un entero
i=2
lista=[]
while (i<=a): #Creamos el ciclo while 
  if a%i == 0: #Un if para comprobar el modulo de cada numero entre el numero dado
    print('El número no es primo') #Si es igual a cero, seria primo, pues es divisible por ese numero distinto de 1
    break
  elif a==i+1: #Un elif para terminar el ciclo, teniendo en cuenta cada numero
    print('El número es primo') #Si se da todos los casos y el if anterior no se cumple, esta linea se imprimirá
    break
  i+=1 #Linea necesaria para que el ciclo while funcione


# In[18]:


prueba = int(input('Escriba un número mayor que 2 '))
menores = list(range(2,prueba))
lista=[]
for i in menores:
  if prueba%i == 0:
    lista.append(i)
  else:
    pass

if lista == []:
  print(str(prueba) + ' es Primo')
else:
  print(str(prueba) + ' no es Primo, sus divisores son:')
  print(lista)

