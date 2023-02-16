#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sympy as sym 
import numpy as np 
from matplotlib import pyplot as plt
x= sym.symbols('x')

print('Bienvenido a la graficadora de funciones trigonométricas \n')
f= input('Inserte la función: ')
dominio= np.linspace(-10,10,5000)
f1= sym.lambdify(x,f,'numpy')
df= sym.diff(f,x)
df1= sym.lambdify(x,df,'numpy')
d2f= sym.diff(df,x)
d2f1= sym.lambdify(x,d2f,'numpy')
t1= sym.simplify(f)
t2= sym.simplify(df)
t3= sym.simplify(d2f)

plt.plot(dominio,f1(dominio),color='red',label=t1)
plt.plot(dominio,df1(dominio),color='blue',label=t2)
plt.plot(dominio,d2f1(dominio),color='green',label=t3)
plt.legend(loc='upper left')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.grid()
plt.show()

