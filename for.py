#Ejemplo de ciclo for y ciclo while

#Agregamos un input para ingresar un numero y hacemos una lista con eso
#Además hacemos dos arreglos vacios
var = int(input('Inserte un número positivo: '))
abc=list(range(0,var,2))
empty=[]
empty2=[]

#Ciclo for para agregar elementos al arreglo vacio
for i in abc:
	empty.append(i+1)

#Ciclo while para agregar elementos al arreglo vacio
j=0 #El ciclo while funciona mientras j sea menor al tamaño de la lista abc
while j<len(abc):
	empty2+=[j]
	j+=1

#Imprimimos los arreglos con sus nuevos elementos
print(empty)
print(empty2)	

vacio = [i+1 for i in abc]	#Declarar arreglos de forma mas eficiente
print(vacio)				#Mostramos este arreglo
print(empty == vacio)		#Verificamos que sea igual al generado con el ciclo for