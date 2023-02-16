import random
import numpy as np
import time
import matplotlib.pyplot as plt

print('Bienvenido a la calculadora de probabilidades!!!\n')
x = int(input('Cuantas veces lanzaremos los dados: '))

inic = time.time()
lista = [random.randint(1,6) for i in range(x)]

lista2 = dict(zip(lista,map(lambda i: lista.count(i),lista)))

order = sorted(lista2)
origin = lista2.keys()
ordenado = {}

for i in order:
	ordenado[i] = lista2[i]

print(ordenado)
final = time.time()
tot = final - inic
print('El tiempo total del experimento es: ',tot)

plt.bar(ordenado.keys(),list(ordenado.values()),color='red')
plt.show()