class Nombre_y_apellido:
	def __init__(self,nombre,apellido):
		self.nombre = nombre
		self.apellido = apellido

	def presentarse(self):
		print('Hi, my name is ' + self.nombre + ' ' + self.apellido)

class Edad_y_genero:
	def __init__(self,edad,genero):
		self.edad = edad
		self.genero = genero

class Persona(Nombre_y_apellido,Edad_y_genero):
	def __init__(self,nombre,apellido,edad,genero,profesion):
		Nombre_y_apellido.__init__(self,nombre,apellido)
		Edad_y_genero.__init__(self,edad,genero)
		self.profesion = profesion

	def __eq__(self,other):

		d1 = self.edad == other.edad
		d2 = self.nombre == other.nombre
		d3 = self.genero == other.genero
		d4 = self.apellido == other.apellido

		return (d1 and d2 and d3 and d4)

	def igual(self,other):

		d1 = self.edad == other.edad
		d2 = self.nombre == other.nombre
		d3 = self.genero == other.genero
		d4 = self.apellido == other.apellido

		return (d1 and d2 and d3 and d4)

	def __add__(self,other):

		new_person = Persona(self.nombre,other.apellido,0,self.genero,other.profesion)

		return new_person

	def __mul__(self,x):

		print('las personas no se multiplican!')

	def __sub__(self,other):

		if(int(self.edad)>int(other.edad)):
			name = self.nombre
			lastname = other.apellido + ' ' + self.apellido
			age = int(self.edad)-int(other.edad)
			gender = self.genero
			print(name, lastname, age, gender)

		elif(int(other.edad)>int(self.edad)):
			name = other.nombre
			lastname = self.apellido + ' ' + other.apellido
			age = int(other.edad)-int(self.edad)
			ocup = self.profesion + ' ' + other.profesion
			gender = other.genero
			print(name,lastname,age,gender,ocup)
		else:
			print('XD')


	def __lt__(self,other):

		if(self.edad > other.edad):

			print(self.nombre + ' es mayor que ' + other.nombre)

		elif(self.edad < other.edad):

			print(self.nombre + ' es menor que ' + other.nombre)

		else:

			print(self.nombre + ' y ' + other.nombre + ' tienen la misma edad')


estudiante = Persona("Ricardo","Zapata",'23','M','Cuber')
estudiante2 = Persona("Ricardo","Zapata",'23','M','Maths')
profesor = Persona('Jesus','Perez','40','M','Teacher')

estudiante-profesor
profesor-estudiante

input()

print(estudiante.nombre)
estudiante.presentarse()
print(estudiante.genero)
print(estudiante.profesion)
print(estudiante == profesor)
print(estudiante == estudiante2)
print(estudiante.igual(estudiante2))
person = estudiante + profesor
print(person.nombre, person.apellido)
estudiante*profesor
estudiante<profesor
estudiante<estudiante2
profesor<estudiante

