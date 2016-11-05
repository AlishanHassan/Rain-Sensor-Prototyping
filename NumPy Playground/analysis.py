import numpy as np
import matplotlib.pyplot as pyplot
import pylab
import scipy
from scipy import signal
from scipy.signal import argrelextrema
import csv as csv
import pandas as pd

filename = 'data.txt'
data = []
header = "header"

def plotData():
    pyplot.plotfile(filename, delimiter=",", skiprows = 1, cols=(1, 2), names=('DateTime', 'Elapsed', 'PiezoValue', 'BucketFlip', 'BucketCount'), marker ='.')
    pyplot.plotfile(filename, delimiter=",", skiprows = 1, cols=(1, 4), names=('DateTime', 'Elapsed', 'PiezoValue', 'BucketFlip', 'BucketCount'), marker ='.')
    pyplot.show()

def printWelcomeStatement():
    print("Hello!")

def readFileData():
    readdata = csv.reader(open(filename))
    #print(readdata)
    global data
    data = []
    for row in readdata:
        data.append(row)
    global header
    header = data[0]
    data.pop(0)

def dataAnalysis():
    print(header)

    elapsed = []
    piezoValue = []
    bucketFlip = []
    bucketCount = []
    for i in range(len(data)):
        elapsed.append(int(data[i][1]))
        piezoValue.append(int(data[i][2]))
        bucketFlip.append(int(data[i][3]))
        bucketCount.append(int(data[i][4]))

    flipPoints = []
    for i in range(len(bucketFlip)):
        if bucketFlip[i-1] == 0 and bucketFlip[i] == 1:
            flipPoints.append(i)

    print(flipPoints)
    print(bucketFlip[7480])

    dct = {}
    for x in range(len(flipPoints)-1):
        dct['dataset_%s' % x] = []
        if x < len(flipPoints) - 1:
            for y in range(flipPoints[x], flipPoints[x+1]):
                dct['dataset_%s' % x].append((elapsed[y], piezoValue[y]))


    print(dct['dataset_12'][0][1])

#    maxi = []
#    maxi.append(dct['dataset_12'][0][1])
#    maxi.append(dct['dataset_12'][1][1])
#    maxi = np.array(maxi)
#    print(maxi)

    for key in dct:
        maxi = []
        c = 0
        for value in dct[key]:
            maxi.append(dct[key][c][1])
            c += 1
        maxi = np.array(maxi)
        maxm = argrelextrema(maxi, np.greater)
        for i in maxm:
            print(maxi[i])
        print(maxm)
        #maxi.append(dct[key])


def printFileData():
    #Must call readFileData() first
    for row in readdata:
        print(row)


#Main function calls below
printWelcomeStatement()
readFileData()
dataAnalysis()

#Other stuff

#data = np.genfromtxt('data.txt', delimiter=',', skip_header=1)

#pylab.plot(data[:1], data[:,2])

#peakind = signal.find_peaks_cwt(data[:,2], np.arange(9000,10000, 1))


#print(data[peakind,2])


#pyplot.plot(data[:,1], data[:,2])
#pyplot.show()



    #for x in range(len(flipPoints)):
    #    globals()['dataset%s' % x] = []
    #    'dataset%s' %x
