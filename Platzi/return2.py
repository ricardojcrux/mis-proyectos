def volumen(length=1, width=1, depth=1):
	return length * width * depth ,  width,  'hola'

result = volumen(width=12,depth=44)

print(result[0:2])

result,width,text = volumen(width=44)

print(result,width,text)