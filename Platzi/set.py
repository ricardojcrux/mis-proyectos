#Ejemplos de conjuntos
country_set = {'col','mex','can','ven'}
print(country_set,type(country_set))
numbers_set = {88,4,3,7,8,6,5,4,1,2,3,71,89,5,6,3,5,7}
print(numbers_set)

set_fromstring = set('Ricardo Zapata Cruz')
print(set_fromstring)

set_fromtuples = set((1,2,3,4,5,6,7))

#And now some differences between tuples and sets

tuple1 = (1,2,3,4,5,1,2,3,4,5)
set1 = {1,2,3,4,5,1,2,3,4,5}
array1 = [1,2,3,4,5,1,2,3,4,5]

list1 = list(set1)

print(type(list1),type(array1))