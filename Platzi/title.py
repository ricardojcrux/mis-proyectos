import numpy as np 
import matplotlib.pyplot as plt

def grafica(a,b,c):
	datos_x = np.linspace(-10,10,100)
	datos_y = [a*i**2 + b*i + c for i in datos_x]

#Dilema del titulo
	if a == 0:
		xx = ''
	elif a == 1:
		xx = 'x^2'
	else:
		xx = str(a) + '*x^2'

	if b == 0:
		x = ''

	elif b == 1:
		if a == 0:
			if c== 0:
				x = 'x'
			elif c!=0:		
				x = ' x'
		elif a!= 0:
			x = ' + x'
		
	else:
		if a == 0:
			if c== 0:
				x = str(b) + '*x'
			elif c!=0:		
				x = str(b) +'*x + '
		elif a!= 0:
			x = ' + ' + str(b) + '*x'

	if c == 0:
		if a==0 and b==0:
			cons = '0'
		else:
			cons = ''
	elif a==0 and b==0:
		cons = str(c)
	else:
		cons = ' + ' + str(c)

	plt.plot(datos_x,datos_y)
	plt.title('Gráfica de : ' + xx  + x + cons)
	plt.grid()
	plt.show()

a=int(input('Ingrese el valor de a: '))
b=int(input('Ingrese el valor de b: '))
c=int(input('Ingrese el valor de c: '))

grafica(a,b,c)
