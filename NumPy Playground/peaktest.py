import numpy as np
import matplotlib.pyplot as pyplot
import pylab
import scipy
from scipy import signal
from scipy.signal import argrelextrema
import csv as csv
import pandas as pd

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 5, 6, 7, 8, 9, 12, 5, 5, 4, 3, 4, 6, 8, 9, 9, 7, 7, 5, 4, 5, 6, 7, 8, 11, 22, 11, 9])

peakind = signal.find_peaks_cwt(data, np.arange(1,len(data)))

print(data[peakind[0]])

#sortId = np.argsort(data)
#data = data[sortId]

maxm = argrelextrema(data, np.greater)

for i in maxm:
    print(data[i])
print(maxm)
