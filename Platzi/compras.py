compras=[
	{
	'producto' : 'arroz',
	'cantidad' : 15,
	'precio' : 10000
	}
]

print('Bienvenido a la lista de compras: ')

def total(compras):
	compras['total'] = int(compras['cantidad']) * int(compras['precio'])
	return compras

def elemento(compras):
	ejemplo = compras[0]
	ejemplo = list(ejemplo.keys())
	element = {i: input(i + ': ') for i in ejemplo}
	return element

while True:
	a = input('Quiere ver la lista de compras (s/n): ')
	if a == 's':
		print(compras)
	if a == 'n':
		b = input('Quiere agregar un nuevo elemento (s/n): ')
		if b == 's':
			element = elemento(compras)
			compras.append(element)
			print(compras)
		if b == 'n':
			compras = list(map(total,compras))
			print(compras)
			print('Gracias por ser y estar!!!')
			break
		else:
			print('Elija una opcion correcta')
	else:
		print('Elija una opcion correcta')