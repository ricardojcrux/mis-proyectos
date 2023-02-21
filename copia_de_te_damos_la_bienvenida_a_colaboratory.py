import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x = sym.symbols("x")
f = input(("introduzca la funcion a graficar ->:"))
g_simbolica = sym.sympify(f)
g_numerica = sym.lambdify(x, g_simbolica,"numpy")
Derivada = sym.diff(f,x)
Derivada1 = sym.lambdify(x,Derivada,"numpy")
Derivada2 = sym.diff(Derivada, x)
Derivada3 = sym.lambdify(x, Derivada2, "numpy")
DominioX=np.linspace(-10,10,1000)
plt.plot(DominioX , g_numerica(DominioX),"green",label=f)
plt.plot(DominioX , Derivada1(DominioX),"red",label=Derivada)
plt.plot(DominioX , Derivada3(DominioX),"blue",label=Derivada2)
plt.grid()
plt.legend()
plt.show()