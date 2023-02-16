msj = '''Bienvenido al conversor de monedas

Seleccione una opcion:

[1] COP-USD
[2] ARS-USD 
[3] MXN-USD

'''
select = input(msj)

def tarea(tipo,valor):
	pesos = float(input('\nIngrese un valor en pesos ' + tipo + ': '))
	dolares = pesos / valor
	dolares = round(dolares,2)
	dolares = str(dolares)
	print('\nTienes $' + dolares + ' dolares')

if select == '1':
	tarea('colombianos', 4438)

elif select == '2':
	tarea('argentinos', 145.49)

elif select == '3':
	tarea('mexicanos',20.20)

else:
	print('\nIngresa una opcion correcta')