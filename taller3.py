import matplotlib.pyplot as plt
import math as m

a=int(input('Inserte el valor de a: '))
b=int(input('Inserte el valor de b: '))
rang=int(input('Inserte el rango: '))

lista=list(range(0,rang+1))
y=[]

for i in lista:
	def function(x,a,b):
		return a*m.exp(b*x)
	x=function(i,a,b)	
	y+= [x]

name= 'gráfico de f(x) = '+ str(a) + 'exp (' + str(b) + 'x)'
print(y)
plt.title(name)
plt.plot(lista,y, color='pink')
plt.grid()
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()