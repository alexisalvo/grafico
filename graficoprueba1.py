from pylab import *
import matplotlib.pyplot as plt  
import numpy as np

#definimos el periodo de la grafica senoidal
periodo = 2
#definimos el array dimensinal
x = np.linspace(0, 10, 100)
#defeinimos la funcion senoidal
y = np.sin(2*np.pi*x/periodo)
#creamos la figura
plt.figure()
#primer grafico
plt.subplot(2,2,1)
plt.plot(x,y,"r")
title ("grafico 1")
#segundo grafico
plt.subplot(2,2,2)
plt.plot(x,y,linestyle = "--",color = "g")
#tercer grafico
plt.subplot(2,2,3)
plt.plot(x,y,"b")
#cuarto grafico
plt.subplot(2,2,4)
plt.plot(x,y,"k")
#mostrar en pantalla
plt.show()