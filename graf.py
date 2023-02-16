from matplotlib import pyplot

def graficador(dominio,*funciones):

	for f in funciones:
		pyplot.plot(dominio,f)
	pyplot.show()
	