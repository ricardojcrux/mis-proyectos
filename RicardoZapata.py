a=20
b=-5
c=31
rad=(b**2)-(4*a*c)
x1=(-b+(rad**(1/2)))/(2*a)
x2=(-b-(rad**(1/2)))/(2*a)

if(x1.imag!=0 and x1.real>0):
	print('la solución es', x1.imag)

if(x2.imag!=0 and x1.real>0):
	print('la solución es', x2.imag)