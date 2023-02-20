import tkinter

window = tkinter.Tk()
window.title('Calculadora Básica')
window.geometry('720x480')

etiq1=tkinter.Label(window, text='Entrada', bg='yellow' ,fg='red',font=('arial',20))
etiq1.place(relx=0.1, y=20)

entry=tkinter.Entry()
entry.place(relx=0.1, y=60)

etiq2=tkinter.Label(window, text='Salida', bg='cyan', fg='blue',font=('arial',20))
etiq2.place(relx=0.7, y=20)

exit= tkinter.Entry()
exit.place(relx=0.7, y=60)

def Cuadrado():
	exit.delete(0,tkinter.END)
	ingreso = float(entry.get())
	cuadrado = ingreso**2
	exit.insert(0,cuadrado)

def Cubo():
	exit.delete(0,tkinter.END)
	ingreso = float(entry.get())
	cuadrado = ingreso**3
	exit.insert(0,cuadrado)

def Borrar():
	entry.delete(0,tkinter.END)
	exit.delete(0,tkinter.END)

boton = tkinter.Button(window, text='Cuadrado', bg='green', command=Cuadrado)
boton.place(relx=0.1, y=100)

boton = tkinter.Button(window, text='Al Cubo', bg='blue', fg='white' ,command=Cubo)
boton.place(relx=0.1, y=130)

boton = tkinter.Button(window, text='Borrar Todo',bg='purple',fg='white',command=Borrar)
boton.place(relx=0.1, y=160)

window.mainloop()