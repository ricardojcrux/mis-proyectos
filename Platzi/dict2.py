import random

countries = ['col','ven','ecu','per','chi']
population = {i: random.randint(1,100) for i in countries}

print(population)

result = {a:b for (a,b) in population.items() if b>20}
print(result)

text = 'Hola, soy Ricardo'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(text)
print(unique)