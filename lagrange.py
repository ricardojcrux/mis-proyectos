import tkinter
from tkinter import filedialog
import numpy as np 
import matplotlib.pyplot as plt 
import h5py
from scipy.interpolate import lagrange

window = tkinter.Tk()
window.title('Data Graphing Program') 
window.geometry('800x600')

title = tkinter.Label(text='Data Graphing Program',bg='black',fg='red',font='Arial,30')
title.place(x=300,y=50)

def leerarchivo():

	global archivo
	archivo = filedialog.askopenfilename(title='Abrir archivo')

	global salida
	salida = tkinter.Entry()
	salida.place(x=50,y=100, width=700,height=30)
	salida.insert(0,archivo)

	global boton2
	boton2 = tkinter.Button(window,text='Generar FL', command=pol)
	boton2.place(x=50,y=150)

def pol():

	global leer 
	leer = h5py.File(archivo,'r')
	
	global x
	x = leer.get('x')
	
	global y
	y = leer.get('y')

	global poly
	poly = lagrange(x, y)

	global coff
	coff = poly.coef

	global lag
	lag = tkinter.Entry()
	lag.place(x=50,y=230, width=100,height=30)
	lag.insert(0,coff)

	fl = tkinter.Label(window, text='Coeficientes FL' ,fg='purple')
	fl.place(x=50,y=200)

	global boton3
	boton3 = tkinter.Button(window,text='Graficar',command=graficar)
	boton3.place(x=50,y=280)

def graficar():
	ini = min(list(x[:]))
	fin = max(list(x[:]))
	x1 = int(ini)
	x2 = int(fin)
	xx = list(range(x1,x2+1))
	yy = []
	for i in xx:
		a = coff[2] + i*coff[1] + (i**2)*coff[0]
		yy+= [a]
	plt.plot(xx,yy,color='red',label='Polinomio')
	plt.plot(x[:],y[:],'*',color='yellow',label='Puntos originales')
	plt.title('Interpolacion de Lagrange')
	plt.legend()
	plt.grid()
	plt.show()
	
	print(x[:],y[:])
	print(xx,yy)

boton1 = tkinter.Button(window,text='Abrir archivo',command=leerarchivo)
boton1.place(x=50,y=50)

#Creamos el menú de opciones -------------------------------------------------------------------

def PagOnline():
	import webbrowser
	webbrowser.open('https://sites.google.com/correounivalle.edu.co/ricardozapatacruz/inicio')

def Borrar():
	salida.delete(0,tkinter.END)
	lag.delete(0,tkinter.END)
	xi.delete(0,tkinter.END)
	xf.delete(0,tkinter.END)

menudo = tkinter.Menu(window)
window.config(menu=menudo)

opc1 = tkinter.Menu(menudo)

menudo.add_cascade(label='Opciones',menu=opc1)
opc1.add_command(label='Nuevo', command= Borrar)
opc1.add_command(label='Info online', command=PagOnline)
opc1.add_command(label='Salir', command= window.quit)

window.mainloop()


