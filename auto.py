import numpy as np
from reader import *
from eulers import *
from optimizer import *
import csv
from scipy import optimize as op

def plot(siu):
    tB = siu[0]
    K = siu[1]
    coordinates = ["RTD5010.csv","RTD5011.csv","RTD5012.csv","RTD5013.csv","RTD5014.csv","RTD5015.csv","RTD5021.csv", "RTD5022.csv","RTD5023.csv","RTD5027.csv","RTD5088.csv"]
    #plotting the points
    leastsquares = []
    for i in range(len(coordinates)):
        xCoords, yCoords = getCoordinates(i)
        #plotting the function for the model
        a = findA(xCoords,yCoords,tB,K)
        xCoordsreal, yCoordsreal, eDict = runEuler(a["aValue"],tB,K)
        leastsquares.append(a["leastSquare"])
    return sum(leastsquares) / len(leastsquares)
siu = [500,0.3]
#siu needs to be a numpi array

siuNumpy = np.array(siu)
op.minimize(plot, siuNumpy, bounds = ((100,900),(0.001,1)),options = {"maxiter":50000})
op.optimizeResult()