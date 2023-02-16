def incremento(x):
	return x + 1

increment = lambda x : x + 1

result = incremento(10)
print(result)

result = increment(10)
print(result)

full_name = lambda first_name , last_name : f'Full name is: {first_name.title()} {last_name.title()}'

nombre = full_name('ricardo','zapata')
print(nombre)

