import numpy as np
import matplotlib.pyplot as pyplot
import pylab
import scipy
from scipy import signal

data = np.genfromtxt('playdata.txt', delimiter=',', skip_header=1)

#pylab.plot(data[:1], data[:,2])





#pyplot.plot(data[:,1], data[:,2])
#pyplot.show()

pyplot.plotfile('playdata.txt', delimiter=",", skiprows = 1, cols=(0,1), names=('time', 'value'), marker ='o')
pyplot.show()


print("hello")
