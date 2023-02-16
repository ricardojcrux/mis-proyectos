persona={}
continuar=True

while continuar:
	clave=input('¿Que datos quieres introducir? ')
	valor=input(clave+' : ')
	persona[clave] =valor
	print(persona)
	decision =input('¿Quieres añadir mas información (s/n)')

	if decision=="n":
		print('el programa se cierra')
		break
	elif decision=='s':
		continuar=True
	else:
		decision= input('Elegir entre si o no (s/n)')	


print('informacion de la persona', persona)