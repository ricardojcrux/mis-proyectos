import numpy as np
numeros = []

for i in range(1,11):
	numeros.append(i*2)

print(numeros)

#Nueva forma de generar lista

numeros_v2 = [np.sqrt(i) for i in range(1,11) if i % 2 == 0]
print(numeros_v2)