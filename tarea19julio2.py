import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import tkinter
from tkinter import filedialog
import h5py 
interfaz = tkinter.Tk()

interfaz.title('Programa graficador de datos')
interfaz.geometry("550x450")

BarraMenu = tkinter.Menu(interfaz)
interfaz.config(menu=BarraMenu)
opciones = tkinter.Menu(BarraMenu)

BarraMenu.add_cascade(label="opciones", menu=opciones)

def AbrirPaginaOnline():
	import webbrowser
	webbrowser.open('https://sites.google.com/correounivalle.edu.co/el-mundo-de-las-mascotas/inicio')

opciones.add_command(label="Info online", command=AbrirPaginaOnline)
opciones.add_command(label="Salir", command=interfaz.quit)


# ABRIR ARCHIVO DE DATOS
def leer_archivo():
	global archivo
	archivo =filedialog.askopenfilename(title='open a file')   

	global salida1
	salida1=tkinter.Entry()
	salida1.place(x=100, y=150, width=700, height=40)
	salida1.insert(0, archivo)
	boton2=tkinter.Button(interfaz, bg='white', text='Generar PL', command = polinomio_lagrange,)
	boton2.place(x=100, y=200)

boton1 =tkinter.Button(interfaz,bg='white', text='abrir archivo', command= leer_archivo)
boton1.place(x=100, y=100)

#POLINOMIO LAGRANGE
def polinomio_lagrange():

	archivoHDF5 = h5py.File(archivo,'r')
	global x
	global y
	x = archivoHDF5.get('x')
	y = archivoHDF5.get('y')
	coff=tkinter.Label(interfaz , text='coeficientes polinomio lagrange',fg='green', font=('Arial',15))
	coff.place(x=100, y=250)
	global poly
	poly = lagrange(x, y)
	global lag
	lag = poly.coef

	global salida2
	salida2=tkinter.Entry()
	salida2.place(x=100, y=250, width=700, height=40,)
	salida2.insert(0, lag)
	boton3=tkinter.Button(interfaz, bg='white', text='Graficar', command = graficar)
	boton3.place(x=100, y=280)
 
def graficar():
	global graficar
	etiqueta1 =tkinter.Label(interfaz , text='Introduzca x inicial',fg='green', font=('Arial',15))
	etiqueta1.place(x=100, y=300)
	global xinicial
	xinicial=tkinter.Entry()
	xinicial.place(x=100,y=350)
 
	etiqueta2 =tkinter.Label(interfaz , text='introduzca x final',fg='green', font=('Arial',15))
	etiqueta2.place(x=200, y=300)
	global xfinal
	xfinal=tkinter.Entry()
	xfinal.place(x=200,y=300)
	boton4=tkinter.Button(interfaz, bg='white', text='Graficar', command = FuncionLineal)
	boton4.place(x=100, y=350)


def FuncionLineal():
	z = int(xinicial.get())
	w = int(xfinal.get())
	xx = list(range(z,w))
	yy = []
	for i in xx:
		a = lag[2] + i*lag[1] + (i**2)*lag[0]
		yy+= [a]
	plt.plot(xx,yy)
	plt.title('grafico de datos del archivo') 
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid()
	plt.show()
    
interfaz.mainloop()



