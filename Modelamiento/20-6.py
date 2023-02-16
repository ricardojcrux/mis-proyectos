#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy import stats

longitud  = [0.1,0.17,0.2,0.25,0.26,0.32,0.4,0.49,0.5,0.58,0.6   ]
periodo   = [0.65,0.79,0.9,1.01,1.10,1.20,1.27,1.34,1.42,1.50,1.55  ]
z=np.sqrt(longitud)
x1= np.array(longitud)
y1= np.array(periodo)

regresion = stats.linregress(z,periodo)
m = regresion.slope 
b = regresion.intercept 

def f(x,m,b):
  return m*x1+b

plt.plot(longitud,periodo,'or')
plt.show()
plt.plot(z,periodo, "or")
plt.plot(z,f(z,m,b), 'o-', color="grey")
plt.show()


# In[3]:


g = (2*np.pi/m)**2
v = (m*2.5)**0.5

print('\n','g ------> ',g)
print(' v ------> ',v)


# In[14]:


n=4
z1= z[:n]
p1= periodo[:n]
print(z1,p1)


# In[26]:


inter = sc.interpolate.lagrange(z1,p1)
zdom = np.linspace(z.min(),z.max(),100)
plt.plot(z1,p1, 'ro')
plt.plot(zdom,inter(zdom),'k')
plt.show()


# In[28]:


inter = sc.interpolate.lagrange(z,periodo)
zdom = np.linspace(z.min(),z.max(),100)
plt.plot(z,periodo, 'ro')
plt.plot(zdom,inter(zdom),'o')
plt.show()

