import numpy as np 
import time
import multiprocessing as mp 
import os

n = int(input('Elija el tamaño de las matriz(1-10000): '))
A = np.random.random(size = (n,n))
B = np.random.random(size = (n,n))
C = np.random.random(size = (n,n))
D = np.random.random(size = (n,n))
E = np.zeros((n,n))

#Haciendo el proceso de multiplicar matrices con el ciclo for
ti = time.time()
for i in range(n):
	for j in range(n):
		for k in range(n):
			E[i,j] += A[i,j]* B[k,j]
tf = time.time()
print('El tiempo de ejecución tradicional es:', tf-ti)

#Haciendo el mismo proceso con una funcion de numpy
ti = time.time()
F = np.dot(A,B)
tf = time.time()
print('El tiempo de ejecución intermedio es:', tf-ti)
print('Mucho mas eficiente, ¿no?')
'''
matrices = [A,B,C,D]

ti = time.time()
def SUMA(v):
	suma=0
	for i in range(len(v)):
		for j in range(len(v)):
			suma = suma + v[i,j]
	return suma

lista = []
for i in matrices:
	s = SUMA(i)
	print(s)
	lista.append(s)


tf = time.time()

print('El tiempo de ejecución es:', tf-ti)
input('Continuar?')

#-----------------------------calculo en paralelo----------------------------------

print('Ejecutar el programa de forma paralela')

cores = 4

print('Procesadores disponibles', cores)
input('Ejecutar?\n')

ambiente = mp.Pool(processes = cores)

inic= time.time()

result = ambiente.map(SUMA, matrices)

print('Resultados de las sumas en paralelo',result)

final = time.time()

print('El tiempo de ejecución es:', final-inic)
'''