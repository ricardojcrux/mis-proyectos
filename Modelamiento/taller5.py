#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('datos.csv')
x=datos[:,0]
y=datos[:,1]
u=np.log(x)
v=np.log(y)

plt.plot(x,y,'-s')
plt.show()
print('\n')
plt.plot(u,v,"-o")
plt.show()

n=len(u)
xi=sum(u)
yi=sum(v)
xiyi=sum(u*v)
xi2=sum(u**2)

den=n*xi2-xi**2
mlog= (n*xiyi-xi*yi)/den
blog= (xi2*yi-xiyi*xi)/den

m=mlog
b=np.exp(blog)

print('\nEl valor de K es: ', b,)
print('El valor de C es: ', m,'\n')

dominio=np.arange(2,31)

k=len(dominio)
ymod=[]
p=0
for i in range(k):
  p = b*(dominio[i]**m)
  ymod.append(p)

plt.plot(x,y,"-o", label='Datos')
plt.plot(dominio,ymod,'-s', label='Modelo')
plt.legend()
plt.show()

valor=b*100**m
print('\n','El valor de y con x evaluado en 100 es: ',valor)

