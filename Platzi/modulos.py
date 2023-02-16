import sys		#Informaciones del sistema
print(sys.path[0])

import re		#Expresiones regulares ¡MUY IMPORTANTE!
text = 'Mi numero es 3013229292, el codigo nacional es 57 y mi numero favorito es el 5'
result = re.findall('[0-9]+',text)
print(result)

import time 	#Modulo para tiempo
hora = time.time()
local = time.localtime()
local = time.asctime(local)
print(hora)
print(local)

import collections	#Util para contar y generar diccionarios
numbers = [1,1,2,1,2,1,4,5,3,3,21,1]
counter = collections.Counter(numbers)
print(counter)
