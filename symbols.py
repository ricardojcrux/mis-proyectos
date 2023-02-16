import sympy as sym 
import numpy as np 
from matplotlib import pyplot as plt
x , y = sym.symbols('x,y')

print(type(x))

a= x**2 + 3 * x + 1
b= 4 * x**2 + 3
c= 2 * sym.sin(x)**2 / sym.cos(x)**2 + sym.pi

print(a+b)
print(c)
print(sym.simplify(c))
input('Break XD')

sym.pprint(sym.simplify(c))
input('Break 1')

d= 3*x + x**2 + 2*x**2 - x
sym.pprint(d)
sym.pprint(sym.simplify(d))
input('Break 2')

print(d.subs(x,1))
input('Break solve')

solu= sym.solve(x**2 - 1, x)
print('La soluciones son :', solu)

f= sym.sqrt(x)
lf= sym.limit(f,x,-5)
df= sym.diff(f,x)
sf= sym.integrate(f,x)

print('Función: ',f)
sym.pprint(f)
print('Límite de la función: ',lf)
sym.pprint(lf)
print('Derivada de la función: ',df)
sym.pprint(df)
print('Integral de la función: ',sf)
sym.pprint(sf)
input('XDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXD')

g= 3*x + x**3/2

gnp= sym.lambdify(x, g, 'numpy')

dominio= np.linspace(0,2*np.pi,100)

plt.plot(dominio, gnp(dominio))
plt.grid()
plt.show()
input('AHORA SIIIIII')

entrada= input('Introduzca la funcion a calcular:')

g2= sym.sympify(entrada)
gnp2= sym.lambdify(x,g2,'numpy')

plt.plot(dominio,gnp2(dominio))
plt.grid()
plt.show()