#!/usr/bin/env python
# coding: utf-8

# #Ejercicio
# -> utilizar el metodo de minimos cuadrados para determinar las constantes.
# 
# -> utilizar el modelo de obtenido para producir una grafica del modelo juntocon los datos para x entre 2 y 30.
# 
# -> estime el valor de Y en x=100.

# In[12]:


import numpy as np
import matplotlib.pyplot as plt

def Lin(A,x,n):
  return np.log(A)+n*np.log(x)

tabla= np.loadtxt("datos.csv")
x=tabla[:,0]
y=tabla[:,1]
w=np.log(x)
z=np.log(y)
plt.plot(x,y,"or-")
plt.grid()
plt.show()
plt.plot(w,z,"s-")
plt.grid()
plt.show()

w=np.array(w)
z=np.array(z)
c=np.column_stack((w,z))

def Lin(x,m,b):
  return (m*x+b)


if len(w) !=len(z):
    print("los datos no tienen las misma longitud")
else:
  N= len(w)

Sx=0
Sy=0
Sxy=0
Sxx=0

for i in range(N):
  Sx+=w[i]
  Sy+=z[i]
  Sxy+=w[i]*z[i]
  Sxx+=w[i]*w[i]

den= N*Sxx - Sx**2
m1=(N*Sxy - Sx*Sy)/den
b1=(Sxx * Sy - Sxy *Sx)/den

m=m1
b=np.exp(b1)

print('\nEl valor de K es: ', b,)
print('El valor de C es: ', m,'\n')

dominio=np.arange(2,31)

k=len(dominio)
ymod=[]
p=0
for i in range(0,k):
  p= b*(dominio[i]**m)
  ymod.append(p)

plt.plot(x,y,"-o", label='Datos')
plt.plot(dominio,ymod,'-s', label='Modelo')
plt.legend()
plt.show()

