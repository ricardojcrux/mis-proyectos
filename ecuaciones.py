import numpy as np 

print('Sistemas de ecuaciones 2x2''\n')
print('ax+by=c\n''dx+ey=f\n')
a=int(input('Inserte valor a: '))
b=int(input('Inserte valor b: '))
c=int(input('Inserte valor c: '))
d=int(input('Inserte valor d: '))
e=int(input('Inserte valor e: '))
f=int(input('Inserte valor f: '))

matriz=np.array([[a,b],[d,e]])
total=np.array([c,f])
det = np.linalg.det(matriz)
print('\n')

if det==0:
	print('No hay soluciones\n')
else:
	mult=d/a
	mat1= matriz[0]
	mat2= matriz[1]
	xmat2= mult*mat1
	nmat2= mat2-xmat2
	newf=f-(c*mult)
	y=newf/nmat2[1]
	x=((b*y)-c)/a
	print('El resultado para X es: ' + str(x) + ' y para Y es: ' + str(y))
	print(mult)
	print(newf)