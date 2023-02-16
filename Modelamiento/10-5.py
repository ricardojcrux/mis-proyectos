#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np  

a1= np.array([1,2,3])
l1= [1,2,3]
b1= np.array([-1,0,1])
c1= a1/b1
print(a1+a1)
print(l1+l1)
print(c1)


# In[ ]:


np.dot(a1,b1)


# In[ ]:


a1@b1


# In[ ]:


def f(x,a,b):
  return a*x+b
x=np.linspace(0,1,10)
y=f(x,2,-1)
print(x)
print(y)


# In[ ]:


z=np.arange(0,2*np.pi,0.1)
y1=np.sin(z)
y2=np.cos(z)

plt.plot(z,y1)
plt.plot(z,y2)
plt.show()


# In[47]:


from google.colab import drive
drive.mount('/content/gdrive')


# In[ ]:




