#!/usr/bin/env python
# coding: utf-8

# In[7]:


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


# In[9]:


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





# In[ ]:


#Proporcionalidad logaritmica

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

