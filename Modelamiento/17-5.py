#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


x= list(range(0,10))
y= list(range(0,10))

c= np.column_stack((x,y))
print(c)


# In[4]:


x1= np.arange(0,10,1)
y1= np.arange(0,10,1)


# In[5]:


x= np.array(x)
y= np.array(y)
c= np.column_stack((x,y))
print(c)


# In[6]:


np.savetxt('archivo.dat', c, header ='Valor x, Valor y')


# In[7]:


cload= np.loadtxt('archivo.dat')
print(cload)


# In[8]:


xload= cload[:,0]
yload= cload[:,1]

print(xload,yload)


# In[9]:


import matplotlib.pyplot as plt
plt.plot(xload,yload,'or-',color='purple')
plt.grid()
plt.show()


# Minimos Cuadrados...

# In[10]:


x= [1.5,2.2,3.,4.,5.,6,6.6]
y= [0.5,2.5,2.6,4,3.5,6,5.5]

if len(x) != len(y):
  print('Los datos no tienen la misma longitud')
else:
  n=len(x)
  


# In[11]:


xi,yi,xiyi,xi2=0.,0.,0.,0.
for i in range(n):
  xi+=x[i]
  yi+=y[i]
  xiyi+=x[i]*y[i]
  xi2+=x[i]*x[i]
print(xi,yi,xiyi,xi2)


# In[12]:


m=(n*xiyi-xi*yi)/(n*xi2-xi**2)
b=(xi2*yi-xiyi*xi)/(n*xi2-xi**2)

print(m,b)


# In[16]:


def f(x,m,b):
  return m*x1+b

plt.plot(x,y,'or',color='blue', label ='data')
plt.plot(x,f(x,m,b),color='gray', label='fit')
plt.legend()
plt.show()


# **SCIPY**

# In[15]:


from scipy import stats


regresion = stats.linregress(x1,y1)
m1 = regresion.slope 
b1= regresion.intercept 

print(m1,b1)

plt.plot(x,f(x,m1,b1),color='gray', label='fit')
plt.show()

