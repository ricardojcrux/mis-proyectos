array=[5.5,True, 2, -35, 100] 
print('Arreglo normal:',array) #Imprime el arreglo
array.append('like')
print('append:',array) #Añade elemento al final del arreglo
array.insert(5,2)
print('insert:',array) #Inserta elemento en el indice indicado
array.remove(2)
print('remove:',array) #Remueve elemento del indice indicado
array.reverse()
print('reverse:',array) #Invierte el orden del arreglo
del array[3]
print('del:',array) #Igual que el remove