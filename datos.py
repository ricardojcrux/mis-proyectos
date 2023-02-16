


#================================================================================
#_____________________GUARDAR DATOS DE FORMA MAS PROFESIONAL_____________________

#Otras formas son vtk, pvd, ...


"""
 
Leon Escobar
Departamento de Matematicas
Unviersidad del Valle

Hierarchical Data Format (MUY USADOS en computacion!!!)


Sistema de guardado orientado a objetos (file objects!). El Archivo de datos sera un OBJETO con ciertos
 atributos, variables locales y metodos!!!!!

""" 

 
import numpy as np 
from  matplotlib import pyplot as plt

#paquete que permite manipular archivos hdf5
import h5py 


#Creamos el objeto archivo!
ArchivoComoObjeto = h5py.File( "MiArchivo2.hdf5", "w")



# Aqui creamos el objeto "archivo como objeto". El tiene varios metodos asociados 
#=> el metodo que necesitamos es: create_dataset !!!!)
x = np.linspace(-4, 2 , 3 )
y = -(x+1)**2+1



ArchivoComoObjeto.create_dataset('x', data= x)
ArchivoComoObjeto.create_dataset('y', data= y)

 
#----------------- abriendo el archivo ----------------------
# para leer el archivo
ArchivoLeido = h5py.File( "MiArchivo2.hdf5" , 'r')

#para saber que datos contiene!!!!!!
input("Para saber los datos que tiene")
print(  ArchivoLeido.keys()  )
input("continuar")


x = ArchivoLeido.get('x')
y = ArchivoLeido.get('y')



plt.plot(x[:],y[:])

input("hola")

plt.xlabel('eje de las x')
plt.ylabel('eje de las y')
plt.title('grafiquito de datos del archivo hdf5')
plt.show()
 



