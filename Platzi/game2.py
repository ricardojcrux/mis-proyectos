import random

def opcion():
	opciones = ('piedra','papel','tijera')
	usuario = input('Piedra, papel o tijera: ')
	usuario = usuario.lower()

	if not usuario in opciones:
		print('Opcion no válida')
		return None, None

	computer = random.choice(opciones)

	print('')
	print('Opcion del usuario: ',usuario)
	print('Opcion de la pc: ',computer)
	return usuario, computer

def ganador(usuario,computer,win_u,win_pc):

	if usuario == computer:
		print('Empate!!!')
	elif usuario == 'piedra':
		if computer == 'papel':
			print('Papel vence a piedra')
			print('Victoria de la pc')
			win_pc +=1
		else:
			print('Piedra vence a tijera')
			print('Victoria del usuario')
			win_u +=1
	elif usuario == 'papel':
		if computer == 'tijera':
			print('Tijera vence a papel')
			print('Victoria de la pc')
			win_pc +=1
		else:
			print('Papel vence a piedra')
			print('Victoria del usuario')
			win_u +=1
	elif usuario == 'tijera':
		if computer == 'piedra':
			print('Piedra vence a tijera')
			print('Victoria de la pc')
			win_pc +=1
		else:
			print('Tijera vence a papel')
			print('Victoria del usuario')
			win_u +=1

	return win_u,win_pc

def juego():
	win_u = 0
	win_pc = 0
	rounds = 1

	while True:
		print('\n' + ('*' * 15))
		print('Round N°: ', rounds)
		print('*' * 15 + '\n')

		print('Victorias del usuario: ', win_u)
		print('Victorias de la pc: ', win_pc)
		rounds += 1

		usuario,computer = opcion()
		win_u,win_pc = ganador(usuario,computer,win_u,win_pc)

		if win_pc == 3:
			print('\n*** EL GANADOR ES LA COMPUTADORA ***')
			break

		if win_u == 3:
			print('\n*** EL GANADOR ES EL USUARIO ***')
			break

juego()