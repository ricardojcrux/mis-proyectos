def funcion(x=0):
	return x**2

def func(x=0,y=0,z=0):
	return x+y+z

def func2(f, x):
	return f(x)+44

num=int(input('Type a number a: '))

a=funcion(num)
print(a)

b=int(input('Type a number b: '))
c=int(input('Type a number c: '))

print(func(a,b,c))
print(func2(func,a))