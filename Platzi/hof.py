def increment(x):
	return x + 1

incremento = lambda x : x+1

def high_func(x,func):
	return x + func(x)

high_func_v2 = lambda x , func : x + func(x)

result = high_func(2,increment)
print(result)

result = high_func_v2(2,incremento)
print(result)