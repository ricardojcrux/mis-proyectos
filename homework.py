import tkinter
from tkinter import filedialog
import numpy as np 
from matplotlib import pyplot as plt 
import h5py

window = tkinter.Tk()
window.title('Graficas')
window.geometry('800x800')

def leerarchivo():

	global archivo

	archivo = filedialog.askopenfilename(title='Abrir archivo')

	global salida

	salida = tkinter.Entry()
	salida.place(x=50,y=400, width=700,height=40)
	salida.insert(0,archivo)

def graficar():

	leer = h5py.File('MiArchivo2.hdf5','r')
	x3 = leer.get('x')
	y3 = leer.get('y')
	plt.plot(x3[:],y3[:])
	plt.grid()
	plt.show()

boton1 = tkinter.Button(window,text='abrir archivo',command=leerarchivo)
boton2 = tkinter.Button(window,text='graficar',command=graficar)
boton1.place(x=200,y=200)
boton2.place(x=400,y=200)

window.mainloop()