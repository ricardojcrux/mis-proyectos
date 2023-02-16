import random
dicc = {}

for i in range(1,5):
	dicc[i] = i * 2

print(dicc)

#Nueva forma de generar diccionarios

dicc_v2 = {i:i*2 for i in range(1,5)}
print(dicc_v2)

countries = ['col','ven','ecu','per','chi']
population = {i: random.randint(1,100) for i in countries}

print(population)

nombres = ['nico','zule','santi']
edades = [12,56,98]

dicc = {nombres[i]:edades[i] for i in range(len(nombres))}
print(dicc)

new_dicc = {a:b for (a,b) in zip(nombres,edades)}
print(new_dicc)