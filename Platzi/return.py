def rango(min,max):
	sum = 0
	for x in range(min,max):
		sum +=x
	return sum

result = rango(1,10)

result2 = rango(result,result+10)
print(result,result2)