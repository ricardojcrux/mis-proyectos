def run():
	lista=[]
	i=1
	while i<100:
		i+=1
		if i % 2 !=0:
			continue
		elif i % 31 == 0:
			break
		lista+=[i]
	print(lista)

if __name__ == '__main__':
	run() 