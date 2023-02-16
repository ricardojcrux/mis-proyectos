import matplotlib.pyplot as plt
import math as m

print('Bienvenido a la calculadora del polinomio')
pol=int(input('De que grado será el polinomio: '))
grado=list(range(pol+1))
num=[]
y=[]
dy=[]
z=0
zz=0
text,tit,title='','',''
final,texto='',''
for i in grado:
	coef=int(input('Ingrese el coeficiente ' + str(i+1) + ': '))
	num+=[coef]
ini=int(input('Inserte el rango inicial: '))
fin=int(input('Inserte el rango final: '))
rango=list(range(ini,fin+1))

for i in rango:
	z=0
	for j in grado:
		a=num[j]
		def funcion(a,b,c):
			return a*pow(b,c)
		x=funcion(a,i,j)
		z+=x	
	y+=[z]

for j in grado:
	text=''
	if num[j]==0:
		''
	else:
		
		if j==0:
			text=str(num[j])
		elif j==1:
			text=str(num[j]) + 'x' 
		else:
			text=str(num[j]) + 'x^' + str(j)
		if pol==j:
			text+='.'
		elif num[j]==0:
			''
		else:
			text+=' + '
	tit+=text
opt=int(input('Elige el color del gráfico (1:rojo, 2:azul, 3:verde): '))
colour=['red','blue','green']
title= 'Gráfico de f(x) = ' + tit
plt.title(title)
plt.plot(rango,y, color=colour[opt-1])
plt.grid()
plt.show()

#Ahora comenzamos con el codigo de la derivada de la función
#PD: Esta linea es para automotivarme a no rendirme... :D

for i in rango:
	zz=0
	for j in grado:
		if j==0:
			''
		elif j==1:
			x=num[j]
			zz+=x
		else:	
			k=j-1
			a=num[j]
			dev=a*k
			def funci(a,b,c):
				return (a)*pow(b,c)
			x=funci(dev,i,k)
			zz+=x	

	dy+=[zz]
print(dy)

for j in grado:
	texto=''
	k=j-1
	if num[j]==0:
		''
	else:
		prod=num[j]*j
		if j==0:
			''
		elif j==1:
			texto=str(prod)
		elif j==2:
			texto=str(prod) + 'x' 
		else:
			texto=str(prod) + 'x^' + str(k)
		if pol==j:
			texto+='.'
		elif j==0:
			''
		elif num[j]==0:
			''
		else:
			texto+=' + '
	final+=texto
xd=int(input('Elige el color del gráfico (1:rojo, 2:azul, 3:verde): '))
colour=['red','blue','green']
name= 'Gráfico de f(x) = ' + final
plt.title(name)
plt.plot(rango,dy, color=colour[xd-1])
plt.grid()
plt.show()