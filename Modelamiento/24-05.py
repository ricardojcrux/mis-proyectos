#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

#Proporcionalidad inversa

def inversa(x,k):
  return k/x

x=np.linspace(1,10,20)

y=inversa(x,3)
z=1/x
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x contra y')
plt.show()

plt.plot(z,y)
plt.xlabel('1/x')
plt.ylabel('y')
plt.title('1/x contra y')
plt.show()


# In[ ]:


#Proporcionalidad exponencial

def inversa(x,a,k):
  return a*np.exp(k*x)

y=inversa(x,0.5,2)
z=np.log(y)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x contra y')
plt.show()

plt.plot(x,z)
plt.xlabel('x')
plt.ylabel('log(y)')
plt.title('x contra log(y)')
plt.show()


# In[ ]:


#Proporcionalidad logaritmica

def inversa(x,a,k):
  return a*np.log(k*x)

y=inversa(x,0.9,2)
w=np.log(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x contra y')
plt.show()

plt.plot(w,y)
plt.xlabel('log(x)')
plt.ylabel('y')
plt.title('log(x) contra y')
plt.show()


# ## **EJERCICIO 24-05** 
# 
# * Utilizar el metodo de minimos cuadrados para determinar la constante C y K
# * Utilizar el modelo obtenido para producir una grafica del modelo junto con los datos para x entre 2 y 30
# + Estime el valor de Y en x = 100

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('datos.csv')
x=datos[:,0]
y=datos[:,1]
v=np.log(x)
u=np.log(y)

plt.plot(x,y,'s')
plt.show()

plt.plot(v,u,"-o")

plt.show()


