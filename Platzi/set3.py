country1 = {'col','bol','mex'}
country2 = {'bol','per'}

#Operaciones entre conjuntos

#Union de conjuntos
country3 = country1.union(country2)
print(country3)
print(country1 | country2)

#Interseccion de conjuntos
country3 = country1.intersection(country2)
print(country3)
print(country1 & country2)

#Diferencia de conjuntos
country3 = country1.difference(country2)
country4 = country2.difference(country1)
print(country3)
print(country1 - country2)
print(country4)
print(country2 - country1)

#Diferencia simétrica
country3 = country1.symmetric_difference(country2)
print(country3)
print(country1 ^ country2)