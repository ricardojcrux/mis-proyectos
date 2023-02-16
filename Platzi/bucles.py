'''
contador = 0
a = 2**contador
while a < 1000:
	a = 2**contador
	print('2 elevado a ' + str(contador) + ' es igual a ' + str(a))
	contador = contador + 1
'''

def run():
	
	LIMIT = 1000000
	contador = 0
	pot = 2**contador

	while pot < LIMIT:
		print('2 elevado a ' + str(contador) + ' es igual a ' + str(pot))
		contador = contador + 1
		pot = 2**contador

if __name__ == '__main__':
	run()