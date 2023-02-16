#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np


# In[7]:


def Euler(ti, tf, N, yi, f):
  '''
  Euler method:
    Dado el intervalo solucion ti,tf, el numero de pasos N y 
    la condicion inicial yi. Aproxima la solucion de la 
    ecuacion diferencial ordinaria de primer orden definida por f(t,y).

    Argumentos:
        ti -> Tipo de variable: bla bla

    Salidas: 
        T -> Tipo
        Y ->
  '''

  delta_t = (tf-ti)/N

  Y = [yi]
  T = [ti]
  for i in range(0,N):
    Y.append(Y[i] + delta_t*f(T[i],Y[i]))
    T.append(T[i] + delta_t )

  return np.array(T), np.array(Y)


# In[8]:


def ef(t,u):
  w2 = 1
  x = u[0]
  v = u[1]
  f0 = v
  f1 = -w2*x
  return np.array([f0,f1])
  

