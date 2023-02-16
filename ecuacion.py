import numpy as np

def lineal(a,b,c,d,e,f):
	matriz = np.array([[a,b],[d,e]])
	result = np.array([c,f])
	det = np.linalg.det(matriz)

	if det == 0:
		a = 'El sistema no tiene soluciones'
		return a

	else:
		y= (d*c - a*f)/(d*b - a*e)
		x= (c - (b*y)) / a
		return x, y

print('Sistemas de ecuaciones 2x2''\n')
print('ax+by=c\n''dx+ey=f\n')

lista = []

for i in range(6):
	lista.append(int(input('Inserte valor: ')))

respuesta = lineal(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])

print(respuesta)