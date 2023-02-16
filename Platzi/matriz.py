import numpy as np

#Creamos una matriz de nxn con valores 0
dim = int(input('Que tamaño tendrá la matriz nxn: '))
matriz = np.zeros((dim,dim))

#Le damos valores a cada celda de la matriz
for i in range(dim):
	for j in range(dim):
		matriz[i,j] = int(input('Inserte el valor de la celda ' + str(i+1) + ',' + str(j+1) + ': '))

print('\nLa matriz ingresada es: \n', matriz)

#Calculamos la determinante de la matriz con NumPy
det = int(np.linalg.det(matriz))
print('\nLa determinante de la matriz es: ', det)

#Creamos la matriz adjunta con valores 0 y calculamos sus valores
adj = np.zeros((dim,dim))
transp = np.zeros((dim,dim))

for i in range(dim):
	for j in range(dim):
		matrix = matriz
		matrix = np.delete(matrix,i,axis=0)
		matrix = np.delete(matrix,j,axis=1)
		if (i+j)%2 == 0:
			adj[i,j] = int(np.linalg.det(matrix))
		else:
			adj[i,j] = (-1)*int(np.linalg.det(matrix))
		transp[j,i] = adj[i,j]

print('\nLa adjunta de la matriz es: \n', adj)
print('\nLa transpuesta de la matriz adjunta es: \n', transp)

#Ahora conseguimos la inversa con el determinante
if det == 0:
	''
else: 
	inversa = (1/det)*transp
	print('\nLa matriz inversa es: \n', inversa)
	print('\n',np.dot(matriz,inversa))