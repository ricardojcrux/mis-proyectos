#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# ---
# ---
# 
# ### 2. Ejercicio de aplicación: Determinación de la energía de activación
# 
# 
# La velocidad de reacción $k$ permite estimar la cantidad de sustancia que se transforma por unidad de tiempo en una reacción química determinada. La ecuación de Arrhenius suministra una relación matemática entre la velocidad de reacción $k$ y la temperatura $T$. De acuerdo con esta ecuación 
# $$k = A\, \exp\left( -~\frac{E_a}{R\cdot T}\right),$$
# donde 
# - $k$ es la velocidad de reacción ($\text{s}^{-1}$)
# - $T$ es la temperatura absoluta ($\text{K}$)
# - $A$ es un factor constante (*factor de frecuencia*, $\text{s}^{-1}$)
# - $E_a$ es la energía de activación de la reacción ($\text{J}\cdot\text{mol}^{-1}$)
# - $R = 8.31~\text{J}\cdot\text{K}^{−1}\cdot\text{mol}^{−1}$ es la constante universal de los gases 
# 
# 

# In[ ]:





# ###**Problema:**
# 
# En un experimento se midió la velocidad de reacción en función de la temperatura para la reacción
# $$\text{CO}(g)+\text{NO}_2(g) \longrightarrow \text{CO}_2(g)+\text{NO}(g),$$
# y se obtuvieron los resultados mostrados en la siguiente tabla: 
# 
# $$
# \begin{aligned}
# &\begin{array}{|c|c|}
# \hline \hline T~\text{(°C)} & k~\text{(1/s)} \\ \hline 
# 325 & 0.028 \\
# 378 & 0.22 \\
# 429 & 1.3 \\
# 475 & 6.0 \\
# 530 & 30 \\\hline
# \end{array}
# \end{aligned}
# $$
# 
# 
# Considerando lo anterior realice las siguientes tareas:
# 
# 1. A partir de la ecuación de Arrhenius, proponga un cambio para las variables experimentales $(T, k)$ que permita obtener una relación lineal entre las variables transformadas. 
# 
# 2. Grafique los datos originales y los transformados. Tome en cuenta el utilizar los marcadores adecuados para los ejes coordenados
# 
# 3. Realice una regresión lineal a los datos transformados y estime el valor del factor de frecuencia y la energía de activación para la reacción. Presente los valores estimados en notación científica
# 
# 4. Usando el modelo obtenido, estime la velocidad de reacción para una  temperatura de 300 °C.
# 
# 5. Almacene en un archivo de texto una tabla que contenga los datos de temperatura en grados Celsius y la velocidad de reacción estimada correspondientes al rango de 300 °C a 550°C en pasos de 10°C. Guarde tambien la gráfica de estos datos junto con los originales en un archivo pdf
# 

# 1) Dada la ecuaciòn de arhenius podemos convertir a -1/t =x y m= Ea/R. Aplicando logartimo a ambos lados de la ecuación tendriamos algo como. 
# lnk = lnA + m*x. la cual tine como ecuación una linea. 
# 
# Por lo tanto, los datos serán de la siguiente forma:

# soluciòn 2. Graficaremos los datos originaels y transformados

# In[10]:


#Empezaremos importando los modulos 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat

#Datos orginales
#sean los datos independientes
a= np.array([325,378,429,475,530])
#datos independientes pero en kelvin
datos_x = a +273.15
datos_y = ([0.028,0.22,1.3,6.0,30]) #datos dependientes

c= -1/(datos_x)
b= np.log(datos_y)
#graficaremos los datos originales
plt.plot(datos_x, datos_y, 'o-') 
plt.xlabel('T(K)')
plt.ylabel('k')
plt.title('Datos originales ') #titulo de la grafica
plt.grid()
plt.show()
#Ahora graficaremos los datos transformados
plt.plot(c, b, '-')
plt.xlabel('-1/T')
plt.ylabel('ln(k)')
plt.title("datos transformados")
plt.grid()
plt.show()


# 3) Realizar una regresiòn lineal con los datos transformados y hallar Ea y A

# 

# In[12]:


# m,b = scipy.optimize.linregress(x,y)

regresion_lineal= stat.linregress(c,b)
inter=regresion_lineal.intercept
m= (regresion_lineal.slope )
# El intercepto es 
print("El valor del intercepto es  : ", inter )
print(" el valor de la pendiente es: ", m)
print('\n')
modelo= inter + c*m
plt.plot(c, b, "o", label= "tendencia lineal" )
plt.plot(c, modelo, label= "grafica lineal")
plt.title ("Tendencial lineal y regresión lineal")
plt.legend()
plt.xlabel("-1/T")
plt.ylabel("lnk")
plt.grid()
plt.show()


# * Para obtener la energía de activación hacemos o siguiente. Sabemos que m= Ea/ R  =16343.543533156666 entonces despejamos Ea y quedaría Ea= R *16343.543533156666  
# * para obtener el factor constante A. Sabemos que lnA = inter = 23.651928687060664 entonces debemos aplicar exponencia. quedaría
# 
# exp(lnA)= exp(23.651928687060664) = A

# In[14]:


#obtendremos la energía de activación 
Ea = m* 8.31
print("La energía de activación es: ", format(Ea,'.1E'), " J* mol ^-1")
A = np.exp(inter)
A1= format(A, '1E')
Ea1= format(Ea,'1E')
print("El valor de factor frecuencia es: ", format(A, '.1E'), "S^-1")


# 4. Usar el modelo obtenido estimar la velocidad de reacciòn para 300 grados centigrados
# 

# In[18]:


#graficaremos el modelo obtenido 
R= 8.31
arreglo_x = np.array(np.linspace(datos_x[0], datos_x[-1]+15, 1000))
arreglo_y = A*np.exp(-(Ea/(R*arreglo_x)))

#graficaremos 
plt.scatter(datos_x, datos_y, color= "red",  label= "datos reales")
plt.plot(arreglo_x,arreglo_y, label= "modelo original")
plt.legend()
plt.grid()
plt.xlabel("T(K)")
plt.ylabel("k^-1")
plt.title("Velocidad de reacción vs Temperatura (k)")
plt.show


# In[15]:


'''
def arhenius( x,y,z,w):
ec= -((y)/(z*w))
ecu= x *np.exp(ec)
return

#queremos evaluar la función en T(k)= 300+273.15 = 573.15
x = A
y =Ea
z= 8.31
w= 573.15

velo = arhenius(x,y,z,w)
print(velo)
'''


# para estimar la velocidad de reacción en 300 grados centigrados.
# conocemos el modelos entonces sería k= A1*np.exp(-Ea1/RT)
# 

# In[19]:


#Tenemos 300 grados centigrados vamos a pasar a kelvin

Tc= 300
Tk= 300+273.15
Vel = A*np.exp(-Ea/(R*Tk))
print(" la velocidad de reacción es: ", format(Vel, '1E'))


# 5. Almacenaremos los datos en un archivo de texto
# 

# In[20]:


#generaremos los datos para guardar
Datos_x= np.arange(300,560, 10)
l =Datos_x +273.15
Datos_y= A*np.exp(-Ea/(R*l))
print(Datos_y)

#preparamos un arreglo para almacenar los datos
datos_dos_columnas= np.column_stack((Datos_x, Datos_y))
print("datos_dos_columnas \n\n ",datos_dos_columnas[0:6,:]," ...\n" )
nombre_archivo = 'resultado_funcion.txt'
encabezado = '  T(C)                     k (s^-1)'
np.savetxt(nombre_archivo, datos_dos_columnas, delimiter='\t', header=encabezado)



# In[22]:


#Graficaremos los datos dados 
#ajustaremos el tamaño de la gráfica 
plt.figure(figsize=(6,3.4))
plt.style.use('default')
#Graficamos los arreglos
plt.plot(Datos_x, Datos_y, color="green", marker= 'o', linestyle ='dashed')
plt.xlabel("T(c)")
plt.ylabel("k (s^-1")
plt.title("Temperatura (c) vs Velocidad de reacción")
plt.grid
# Guarda la gráfica un archivo
plt.savefig('grafico_funcion.png', dpi=150)
plt.savefig('grafico_funcion.pdf', dpi=150)
plt.show

#Graficaremos los datos dados 
#ajustaremos el tamaño de la gráfica 
plt.figure(figsize=(6,3.4))
plt.style.use('default')
#Graficamos los arreglos
plt.plot(a, datos_y, color="red", marker= 'o', linestyle ='dashed')
plt.xlabel("T(c)")
plt.ylabel("k (s^-1")
plt.title("Temperatura (c) vs Velocidad de reacción")
plt.grid
# Guarda la gráfica un archivo
plt.savefig('grAfico_funcion.png', dpi=150)
plt.savefig('grAfico_funcion.pdf', dpi=150)
plt.show


# In[ ]:




