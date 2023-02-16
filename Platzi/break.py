def run():
	lista=[]
	for i in range(1001):
		if i % 2 !=0:
			continue
		lista+=[i]
	print(lista)

	texto = input('Ingrese un texto: ')
	for a in texto:
		if a == 'O':
			break
		print(a)

if __name__ == '__main__':
	run() 