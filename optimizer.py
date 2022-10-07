import numpy as np
from reader import *
from eulers import *
from matplotlib import pyplot as plt

def checkLeastSquare(xCoord, yCoord, eDict):
    total = 0
    for i in range(len(xCoord)):
        total += (eDict[xCoord[i]] - yCoord[i]) ** 2
    return total

def findA(xCoord,yCoord,tB,K):
    stop = False
    a = 0.00005
    maxIter = 15
    stepSize = 0.00001
    iterations = 0
    min_value = {"aValue": 0, "leastSquare": np.Infinity}
    while not stop:
        exCoord, eyCoord, eDict = runEuler(a,tB,K)
        v = checkLeastSquare(xCoord,yCoord,eDict)
        if v <= min_value["leastSquare"]:
            min_value["aValue"] = a
            min_value["leastSquare"] = v
            
        if iterations >= maxIter:
            stop = True
        else:
            iterations += 1
            a += stepSize
            
    return min_value