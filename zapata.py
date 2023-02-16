lista=[]
persona={}
continuar=True
a=int(input('Número de diccionarios: '))
rango=list(range(0,a))

for i in rango:
	persona={}
	print('Bienvenido')
	print('')
	while continuar:
		clave=input('¿Que datos quieres introducir? ')
		valor=input(clave+' : ')
		persona[clave] =valor
		print(persona)
		decision =input('¿Quieres añadir mas información (s/n)')

		if decision=="n":
			print('Gracias por la información')
			lista.append(persona)
			break
		elif decision=='s':
			print('Continuemos')
			continuar=True
		else:
			decision= input('Elegir entre si o no (s/n)')	

	

print(lista)

c=(int(input('Consulta el libro necesario: '))-1)
print(lista[c])
