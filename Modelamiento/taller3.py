#!/usr/bin/env python
# coding: utf-8

# In[6]:


#utilizamos la libreria matplotlib para el grafico
import matplotlib.pyplot as plt
#declaramos los valores de los coeficientes
a,b,c,d=12,5,6,8
#creamos la lista donde irán los valores de x & y
listax=list(range(-20,21,1))
listay=[]
#creamos la funcion polinomica
def polinomio(a,b,c,d,x):
  return a*pow(x,3)+b*pow(x,2)+c*x+d
#creamos un ciclo for para conseguir los valores de y
for i in listax:
  y=polinomio(a,b,c,d,i)
  listay+=[y]
#para la grafica definimos el rango y luego la mostramos
plt.plot(listax,listay)
plt.show()

