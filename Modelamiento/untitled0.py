#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt

x=list(range(10))
y=x

plt.plot(x,y)
plt.show()


# In[19]:


def Cuadratica(x,a,b,c):
  return a*x**2 + b*x + c


# In[24]:


x=[]
x0, xf = 0, 2
h = 0.1
n = 20
for i in range(n+1):
  x.append(x0 + i*h)
print(x)

y=[]

a, b, c = 1, 3, -2
for i in range(n+1):
  y.append(Cuadratica(x[i],a,b,c))
print(y)
plt.plot(x,y)
plt.show()

