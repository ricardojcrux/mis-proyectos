class Felinos:

	propietario = 'Ricardo'

	def __init__(self,nombre_felino,tipo_felino,color_felino):

		self.nombre= nombre_felino
		self.tipo  = tipo_felino
		self.color = color_felino

	def saludo(self):
		return self.nombre + ' dice: Miau'

	def comer(self,hambre):
		if hambre == 'y':
			return self.nombre + ' va a comer'
		else:
			return self.nombre + ' no va a comer'

	def dormir(self,sueno):
		if sueno == 'y':
			return self.nombre + ' va a dormir'
		else:
			return self.nombre + ' no va a dormir'

objeto1 = Felinos('onix','gato','negro')
objeto2 = Felinos('simba','leon','dorado')

a=input('¿el gato tiene hambre? (y/n):')
b=input('¿el gato tiene sueño? (y/n):')
print(type(objeto1))
print(objeto1.nombre,objeto1.tipo,objeto1.color)
print(objeto2.nombre,objeto2.tipo,objeto2.color)
print(objeto1.propietario, objeto2.propietario)
print(objeto1.saludo())
print(objeto1.comer(a))
print(objeto1.dormir(b))