import numpy as np 
import time
import multiprocessing as mp 

n = int(input('Elija el tamaño de las matriz (1-10000): '))

def matriz(n):
	x = np.random.random(size = (n,n))
	return x

A = matriz(n)
B = matriz(n)
C = matriz(n)
D = matriz(n)
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
input('Mucho mas eficiente, ¿no?')

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
	s = int(SUMA(i))
	lista.append(s)

print(lista)

tf = time.time()

print('El tiempo de ejecución es:', tf-ti)

input('Continuar?')

print('Ejecutar el programa de forma paralela')
cores = 2

print('Procesadores disponibles', cores)
input('Ejecutar?\n')

ambiente = mp.Pool(processes=cores)

inic= time.time()

if __name__ == '__main__':
	result = ambiente.map(SUMA, matrices)
	print('Resultados de las sumas en paralelo',result)

final = time.time()

print('El tiempo de ejecución es:', final-inic)
