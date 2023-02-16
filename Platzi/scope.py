precio = 100

def inc():
	global result #			Si declaro la variable como global
	result = precio + 100 #	la puedo usar en todo el código por jerarquia
	return result

print(precio+2)
print(inc())
print(result)