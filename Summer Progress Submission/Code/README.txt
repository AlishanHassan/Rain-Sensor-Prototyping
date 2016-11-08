Python 3 is required with Numpy and Scipy installed. Run in shell, no command line arguments needed. 

The files analysis.py and plotData.py are identical, but simply call different functions. plotData.py simply takes a data file (currently hardcoded as data.txt) and produces plots
for both the piezoelectric data and the tipping bucket data. analysis.py runs a full data analysis and outputs a function of best fit for the provided data, while plotting the 
function against the data points as well. 

To use different data files, simply change the filename variable to the appropriate file. 

This program takes the data collected from seriallogger.py and performs a data analysis. It is capable of plotting the data and finding a function of best fit using least squares.
The current functinoality reads in the data from the file and separates the data into a dictionary for each bucket flip. A bucket flip represents .01" of rainfall, and when using 
timestamps, can determine the instantaneous rainfall rate. For each of the bucket flips, the peak points for the piezoelement readings are found and are then added up. Because 
the zero value for the piezoelement is not 0, the prune value is used to remove peaks that are likely not from a raindrop (set to 15 currently for non-amplified setups). The method
of summation is linear (although squared sums were also tested) by default but can be easily modified. The leastSquares function runs a least square analysis using the summed peak 
values and the ground truth rainfall rate, producing linear, quadratic, cubic, quartic, and (if so desired), degree 10 functions. Functions of other degrees can easily be added. 
leastSquares outputs the produced functions and produces plots repesenting the fits. The program also contains functions to find errors, use custom functions aside from least square
outputs, and a way to find total error. 