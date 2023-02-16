import h5py

class espaciovectorial:
	dim = '3'
	def __init__(self,elem1,elem2,elem3):
		self.elem1 = elem1
		self.elem2 = elem2
		self.elem3 = elem3
		self.comp = [elem1,elem2,elem3]
		self.eucl = ((elem1**2)+(elem2**2)+(elem3**2))**0.5
		self.f = 0

	def __add__(self,other):
		suma = espaciovectorial((self.elem1)+(other.elem1),(self.elem2)+(other.elem2),(self.elem3)+(other.elem3))
		return suma

	def __sub__(self,other):
		resta = espaciovectorial((self.elem1)-(other.elem1),(self.elem2)-(other.elem2),(self.elem3)-(other.elem3))
		return resta

	def __mul__(self,other):
		mult = espaciovectorial((self.elem1)*(other.elem1),(self.elem2)*(other.elem2),(self.elem3)*(other.elem3))
		return mult

	def norma(self):
		x = self.elem1 / self.eucl
		y = self.elem2 / self.eucl
		z = self.elem3 / self.eucl
		self.f = [x,y,z]
		print(self.f)

vector1 = espaciovectorial(4,12,1)
vector2 = espaciovectorial(3,5,10)

suma = vector1+vector2
resta = vector1-vector2
mult = vector1*vector2
print('El vector 1 es: ',vector1.comp, vector1.eucl)
print('El vector 2 es: ',vector2.comp, vector2.eucl)
print('La suma es: ',suma.comp,suma.eucl)
print('La resta es: ',resta.comp,resta.eucl)
print('La multiplicación es: ',mult.comp,mult.eucl)
vector1.norma()
vector2.norma()
suma.norma()
resta.norma()
mult.norma()

archivo = h5py.File('vs.hdf5','w')

archivo.create_dataset('vector1',data=vector1.comp)
archivo.create_dataset('vector2',data=vector2.comp)
archivo.create_dataset('suma',data=suma.comp)
archivo.create_dataset('resta',data=resta.comp)
archivo.create_dataset('mult',data=mult.comp)
archivo.create_dataset('norma1',data=vector1.f)
archivo.create_dataset('norma2',data=vector2.f)
archivo.create_dataset('normasuma',data=suma.f)
archivo.create_dataset('normaresta',data=resta.f)
archivo.create_dataset('normamult',data=mult.f)
archivo.close()
