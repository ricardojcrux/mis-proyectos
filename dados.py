import random, time, numpy as np, matplotlib.pyplot as plt

print('Bienvenido a la calculadora de probabilidades!!!\n')
x = int(input('Cuantas veces lanzaremos los dados: '))

inic = time.time()
lista = [random.randint(1,6) for i in range(x)]
lista = sorted(lista)
lista2 = dict(zip(lista,map(lambda i: lista.count(i),lista)))
print(lista2)

final = time.time()
tot = final - inic
print('El tiempo total del experimento es: ',tot)

plt.bar(lista2.keys(),list(lista2.values()),color='red')
plt.show()