msj = '''Bienvenido al conversor de monedas

Seleccione una opcion:

[1] COP-USD
[2] ARS-USD 
[3] MXN-USD

'''
select = input(msj)
valor1 = 4438
valor2 = 145.49
valor3 = 20.20

if select == '1':
	pesos = float(input('\nIngrese un valor en pesos: '))
	dolares = pesos / valor1
	dolares = round(dolares,2)
	dolares = str(dolares)
	print('\nTienes $' + dolares + ' dolares')

elif select == '2':
	pesos = float(input('\nIngrese un valor en pesos: '))
	dolares = pesos / valor2
	dolares = round(dolares,2)
	dolares = str(dolares)
	print('\nTienes $' + dolares + ' dolares')

elif select == '3':
	pesos = float(input('\nIngrese un valor en pesos: '))
	dolares = pesos / valor3
	dolares = round(dolares,2)
	dolares = str(dolares)
	print('\nTienes $' + dolares + ' dolares')

else:
	print('\nIngresa una opcion correcta')