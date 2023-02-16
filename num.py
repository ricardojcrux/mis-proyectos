import numpy as np 

lista = [1,2,4]
array = np.array([1,2,4])
array2 = np.array([2,0,0])

print(array+array)
print(array+array2)
print(array*array)

input('wait''\n')

ldl=[[1,2,3],[4,5,6],[7,8,9]]
matriz= np.array(ldl)
print(type(matriz))
print(matriz[1:])

input('wait''\n')

#Investigar metodos de sistemas de ecuaciones
#Tambien investigar inversa, traspuesta y determinante de una ecuación
det = int(np.linalg.det(matriz))
print(matriz@array)
print('\n')
print(matriz@matriz)
print(array@matriz)
print('\n')
print(det)

print(dict(zip(array,array2)))