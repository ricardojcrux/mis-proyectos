import tkinter
import matplotlib.pyplot as plt 

window = tkinter.Tk()
window.title('Programa para Graficar Rectas')
window.geometry('720x480')

etiq1= tkinter.Label(window, text='La formula de la recta es mx+b' ,fg='green',font=('arial',20))
etiq2= tkinter.Label(window, text='m:',fg='red',font=('arial',15))
etiq3= tkinter.Label(window, text='b:',fg='blue',font=('arial',15))
etiq4= tkinter.Label(window, text='Initervalo inicial',font=('arial',15))
etiq5= tkinter.Label(window, text='Intervalo final', font=('arial',15))
etiq6= tkinter.Label(window, text='Intervalo de la grafica' ,font=('arial',20))

etiq1.place(relx=0.1, y=20)
etiq2.place(relx=0.1, y=70)
etiq3.place(relx=0.1, y=100)
etiq4.place(relx=0.1, y=170)
etiq5.place(relx=0.1, y=200)
etiq6.place(relx=0.1, y=130)

m=tkinter.Entry()
m.place(relx=0.5, y=70)

b=tkinter.Entry()
b.place(relx=0.5, y=100)

inic=tkinter.Entry()
inic.place(relx=0.5, y=170)

final=tkinter.Entry()
final.place(relx=0.5, y=200)

def Grafica():
	dato1 = float(m.get())
	dato2 = float(b.get())
	dato3 = float(inic.get())
	dato4 = float(final.get())

	x=[dato3,dato4]
	one = (dato1*dato3)+dato2
	two = (dato1*dato4)+dato2
	y=[one,two]

	plt.plot(x,y)
	plt.xlim(dato3,dato4)
	plt.grid()
	plt.show()

def Borrar():

	m.delete(0,tkinter.END)
	b.delete(0,tkinter.END)
	inic.delete(0,tkinter.END)
	final.delete(0,tkinter.END)

boton = tkinter.Button(window, text='Graficar', bg='blue', fg='white' ,command=Grafica)
boton.place(relx=0.2, y=250)

boton = tkinter.Button(window, text=' Borrar ', bg='red', fg='white' ,command=Borrar)
boton.place(relx=0.5, y=250)

#------------------------------------------------------------------------------------
def PagOnline():
	import webbrowser
	webbrowser.open('https://docs.python.org/3/library/tk.html')

menudo = tkinter.Menu(window)
window.config(menu=menudo)

opc1 = tkinter.Menu(menudo)
menudo.add_cascade(label='Opciones',menu=opc1)

opc1.add_command(label='Nuevo'	, command= Borrar)
opc1.add_command(label='Info online'	, command=PagOnline)
opc1.add_command(label='Salir'	, command= window.quit)

window.mainloop()