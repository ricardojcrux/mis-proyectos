#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
  a= int(input('Escriba un numero entero: '))
  b= a%2
  if (b!=0):
   print('a es impar')
  else:
    print('a es par')
except:
  print('El número está mal escrito, escríbalo nuevamente')


# In[ ]:


array=[1,2,3,4,5,6,7,8,9,10]
l=len(array)
print('Longitud del array:', l)
for num in array:
  print(num)


# In[ ]:


a=45
for i in range(0,a+1):
  if i%2 == 0:
    continue
  if i==53:
    break
  print(i)


# In[ ]:


a=int(input('Escriba un número '))
liste=list(range(2,a))
for x in liste:
  if a%x == 0:
    print('El número no es primo')
    break
  elif a==x+1:
    print('El número es primo')
    break


# In[ ]:


hola=list(range(1,51))
sum=0
for i in hola:
    sum+=i
print(sum)


# In[ ]:


def SUMAS(hol):
  hol=list(range(1,10))
  suma=0
  for i in range(len(hol)):
    suma+=hol[i]
  return suma
df=SUMAS(8)
print(df)


# In[ ]:





# In[1]:


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

