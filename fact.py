n = int(input('Ingrese un numero: '))
def fact(x):
	if x>0:
		return x*fact(x-1)
	else:
		return 1
print('El factorial del numero ' + str(n) + ' es ' + str(fact(n)))  