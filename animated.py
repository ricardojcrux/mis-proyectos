import numpy as np 
import matplotlib.pyplot as plt 

n= 100
t= np.linspace(0,4*np.pi,n)
y= np.sin(t)
y2=np.cos(t)
nro=len(t)

for i in range(nro): 
	plt.plot(t[i],y[i], color='orange',marker='+')
	plt.plot(t[i],y2[i], color='black', marker='.')
	plt.xlim((0,4*np.pi))
	plt.ylim((-2,2))
	plt.pause(0.05)
plt.show()

for i in range(nro):
	plt.plot(t[i],y[i], color='navy',marker='*')
	plt.grid(color='silver')
	plt.xlim((0,4*np.pi))
	plt.ylim((-2,2))
	plt.title('Animation')
	plt.pause(0.01)
plt.show()