country_set = {'col','mex','can','ven'}

size = len(country_set)
print(size)

print('ven' in country_set)
country_set.add('per')
print(country_set)
country_set.add('per')
print(country_set)

set1 = {8,12}

set1.add(1)
print(set1)
set1.update((1,2,3,4))
print(set1)
set1.discard(15)
print(set1)
set1.remove(12)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)