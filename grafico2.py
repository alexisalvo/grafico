from pylab import *
import matplotlib.pyplot as plt
import numpy as np

x = linspace(0, 5, 10, 20)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('dias')
ylabel('individuo')
title('Grafico')
show()
