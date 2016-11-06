import numpy as np
import matplotlib.pyplot as pyplot
import pylab
import scipy
from scipy import signal
from scipy.signal import argrelextrema
import csv as csv
import pandas as pd
import scipy.optimize as scimin
import matplotlib.pyplot as mpl
from scipy.optimize import leastsq
import matplotlib.patches as mpatches

filename = 'data.txt'
data = []
header = "header"
pruneValue = 15

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
    #print(header)

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
    #print(bucketFlip[7480])

    dct = {}
    for x in range(len(flipPoints)-1):
        dct['dataset_%s' % x] = []
        if x < len(flipPoints) - 1:
            for y in range(flipPoints[x], flipPoints[x+1]):
                dct['dataset_%s' % x].append((elapsed[y], piezoValue[y]))

    #print(dct['dataset_12'])
    #print(dct['dataset_12'][0][1])

#    maxi = []
#    maxi.append(dct['dataset_12'][0][1])
#    maxi.append(dct['dataset_12'][1][1])
#    maxi = np.array(maxi)
#    print(maxi)


    dataset_attr = []

    for key in dct:
        elapsed_time = dct[key][len(dct[key])-1][0] - dct[key][0][0]
        maxi = []
        c = 0
        for value in dct[key]:
            maxi.append(dct[key][c][1])
            c += 1
        maxi = np.array(maxi)
        maxm = argrelextrema(maxi, np.greater)
        #this is where we've got the peak points from each of the data sets, do calculations here

        for i in maxm:
            sum = 0
            #print(maxi[i])
            for j in maxi[i]:
                if maxi[i][j] > pruneValue:
                    sum += maxi[j]
            #print(key)
            #print(sum)
            dct[key].insert(0, elapsed_time) #add the elapsed time to the dictionary
            dct[key].insert(0, sum) #add the sum to the dictionary

    #print(dct['dataset_12'])


    for key in dct:
        actual_rainfall = 0.01/((dct[key][1])/1000/3600) #rainfall rate in in/hr
        computed_rainfall = dataComputation(dct[key][0], 0, 0, 0, 0)
        error = errorCompute(computed_rainfall, actual_rainfall)
        print(actual_rainfall, computed_rainfall, error)
        #print(maxm)
        #maxi.append(dct[key])
        dct[key].insert(0, actual_rainfall)
        dct[key].insert(1, computed_rainfall)
        dct[key].insert(2, error)

    avgError = totalError(dct)
    print(avgError)

    leastSquares(dct)

    #Dictionary structure at this point in a key: {Actual Rainfall, Computed Rainfall, Error, Sum of Peaks, Elapsed Time, Individual Data Points....}

    #print(dct['dataset_12'])

def printFileData():
    #Must call readFileData() first
    for row in readdata:
        print(row)

def dataComputation(value, alpha, beta, gamma, delta):
    #this applies some sort of function to modify the sum

    #polynomial function of degree 3
    s = alpha * pow(value, 3)  + beta * pow(value, 2) + gamma * value + delta

    return s

def errorCompute(u, v):
    #this computes the error for one of the data sets
    w = abs(u - v)
    return w

def totalError(e):
    sumOfErrors = 0
    f = 0
    for key in e:
        sumOfErrors += e[key][2]
        f += 1
    g = sumOfErrors / f
    return g

def leastSquares(w):
    x = []
    y = []
    for key in w:
        x.append(w[key][0])
        y.append(w[key][3])
    x = np.array(x)
    y = np.array(y)

    funcLine = lambda tpl,x :  tpl[0]*x+tpl[1]
    funcQuad = lambda tpl,x :  tpl[0]*x**2+tpl[1]*x+tpl[2]
    funcCubic = lambda tpl,x : tpl[0]*x**3+tpl[1]*x**2+tpl[2]*x+tpl[3]
    funcQuartic = lambda tpl,x:tpl[0]*x**4+tpl[1]*x**3+tpl[2]*x**2+tpl[3]*x+tpl[4]
    func10 = lambda tpl,x :    tpl[0]*x**10+tpl[1]*x**9+tpl[2]*x**8+tpl[3]*x**7+tpl[4]*x**6+tpl[5]*x**5+tpl[6]*x**4+tpl[7]*x**3+tpl[8]*x**2+tpl[9]*x+tpl[10]

    #Linear
    func=funcLine
    ErrorFunc=lambda tpl,x,y: func(tpl,x)-y
    tplInitial1=(1.0,2.0)
    tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x,y))
    print("Linear fit ",tplFinal1)
    xx1 = np.linspace(x.min(),x.max(),50)
    yy1 = func(tplFinal1,xx1)

    #Quadratic
    func=funcQuad
    tplInitial2 = (1.0,2.0,3.0)
    tplFinal2,success=leastsq(ErrorFunc,tplInitial2[:],args=(x,y))
    print("Quadratic fit" ,tplFinal2)
    xx2 = xx1
    yy2 = func(tplFinal2,xx2)

    #Cubic
    func=funcCubic
    tplInitial3 = (1.0, 2.0, 3.0, 4.0)
    tplFinal3,success=leastsq(ErrorFunc,tplInitial3[:],args=(x,y))
    print("Cubic Fit", tplFinal3)
    xx3 = xx2
    yy3 = func(tplFinal3, xx3)

    #Quartic
    func = funcQuartic
    tplInitialQuartic=(1.0, 2.0, 3.0, 4.0, 5.0)
    tplFinalQuartic,success=leastsq(ErrorFunc,tplInitialQuartic[:],args=(x,y))
    print("Quartic Fit", tplFinalQuartic)
    xx4 = xx3
    yy4 = func(tplFinalQuartic, xx4)

    #Degree 10
    func = func10
    tplInitial10=(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0)
    tplFinal10,success=leastsq(ErrorFunc,tplInitial10[:],args=(x,y))
    print("Degree 10 Fit", tplFinal10)
    xx10 = xx1
    yy10 = func(tplFinal10, xx10)

    pyplot.plot(xx1,yy1,'r-',x,y,'bo',xx2,yy2,'g-',xx3,yy3,'b-',xx4,yy4,'m-')

    #plot with degree 10 function
    #pyplot.plot(xx1,yy1,'r-',x,y,'bo',xx2,yy2,'g-',xx3,yy3,'b-',xx4,yy4,'m-',xx10,yy10,'k-')

    red_patch = mpatches.Patch(color='red', label='Linear')
    green_patch = mpatches.Patch(color='green', label='Quadratic')
    blue_patch = mpatches.Patch(color='blue', label='Cubic')
    magenta_patch = mpatches.Patch(color='magenta', label='Quartic')
    #black_patch = mpatches.Patch(color='black', label='Degree 10')
    pyplot.legend(handles=[red_patch, green_patch, blue_patch, magenta_patch])
    #pyplot.legend(handles=[red_patch, green_patch, blue_patch, magenta_patch, black_patch])
    pyplot.xlabel('Actual Rainfall (in/hr)')
    pyplot.ylabel('Pruned Sum of Peaks')

    pyplot.show()

#Main function calls below
printWelcomeStatement()
#plotData()
readFileData()
dataAnalysis()

#Other stuff below

#data = np.genfromtxt('data.txt', delimiter=',', skip_header=1)

#pylab.plot(data[:1], data[:,2])

#peakind = signal.find_peaks_cwt(data[:,2], np.arange(9000,10000, 1))


#print(data[peakind,2])


#pyplot.plot(data[:,1], data[:,2])
#pyplot.show()



    #for x in range(len(flipPoints)):
    #    globals()['dataset%s' % x] = []
    #    'dataset%s' %x
