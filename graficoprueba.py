from pylab import *
import matplotlib.pyplot as plt  
import numpy as np

lista1 = [1,2,3,4,8,16,32,64]
lista2 = [2,5,7,9,0,4,2,50]
lista3 = [0.3,2,73,1, 30,0.7]
plt.xlabel("Dia")
plt.ylabel("Temperatura")
plt.plot(lista1,marker = "x",linestyle = "--",color = "g",label = "enero")
plt.plot(lista2,marker = ".",linestyle = ":", color = "r",label = "febrero")
plt.plot(lista3,marker = "h",linestyle = "-.",color ="b", label = "marzo")
title("grafico")
plt.legend()
plt.show()