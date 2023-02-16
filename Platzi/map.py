import numpy as np

numbers = [1,2,3,4]
numbers_v2 = []

for i in numbers:
	numbers_v2.append(i * 2)

#El esquema del map es: map(lambda x : transformación de x, arreglo de x's)
numbers_v3 = list(map(lambda i : i*2,numbers))
numbers_v4 = list(map(lambda i : np.sqrt(i) + np.pi,numbers_v3))

print(numbers)
print(numbers_v2)
print(numbers_v3)
print(numbers_v4)
print('')

numeros = [5,6,7]

print(numbers)
print(numeros)
print('')

result = list(map(lambda x,y : x + y, numbers,numeros))

print(result)