import numpy as np 

#Consultamos cuantos datos hay en total
k = int(input('Cuantos elementos tendrá el conjunto: '))
lista = np.zeros(k)
tot,num,var = 0,0,0

#Creamos ciclo for para ingresar datos al conjunto
for i in range(k):
	a = float(input('Inserte una cantidad: '))
	lista[i] = a
	tot += a

#Calculamos la media
avg = tot / k

print('\nLos elementos son: ',lista, '\n')
print('El promedio de los elementos es: ', avg ,'\n')

#Hacemos un ciclo for para calcular la varianza y la desviacion estandar
for i in range(k):
	num = (lista[i]-avg)**2
	var += num

varianza = var / k
desv = np.sqrt(varianza)

print('La varianza es: ', varianza,'\n')
print('La desviacion tipica es: ',desv)
