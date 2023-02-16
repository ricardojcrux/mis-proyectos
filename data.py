import numpy as np
import matplotlib.pyplot as plt
import h5py

archivo = h5py.File('datos.hdf5','w')

x = np.linspace(0,100)
y = x**2

archivo.create_dataset('x', data=x)
archivo.create_dataset('y', data=y)

read = h5py.File('datos.hdf5','r')

x = read.get('x')
y = read.get('y')

plt.plot(x[:],y[:])
plt.grid()
plt.show()
