persona,decision={},'s'
print('Bienvenido a la lista de compra\n')

while True:
	if decision == "n":
		print('El programa se cierra')
		break
	elif decision == 's':
		clave = input('¿Que datos quieres introducir?: ')
		valor = input(clave+' : ')
		persona[clave] = valor
		print(persona)
		decision = input('¿Quieres añadir mas información (s/n): ')
	else:
		decision = input('Elegir entre si o no (s/n): ')	

print('informacion de la persona:', persona)