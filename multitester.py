from matplotlib import pyplot as plt
import numpy as np
from reader import *
from eulers import *
from optimizer import *
import csv

def plot(i,tB,K):
    coordinates = ["RTD5010.csv","RTD5011.csv","RTD5012.csv","RTD5013.csv","RTD5014.csv","RTD5015.csv","RTD5021.csv", "RTD5022.csv","RTD5023.csv","RTD5027.csv","RTD5088.csv"]
    #plotting the points
    xCoords, yCoords = getCoordinates(i)
    #plotting the function for the model
    a = findA(xCoords,yCoords,tB,K)
    xCoordsreal, yCoordsreal, eDict = runEuler(a["aValue"],tB,K)
    return a["leastSquare"]


def avgLS(tB,K):
    newlist = []
    for i in range(0,11):
        newlist.append(plot(i,tB,K))
    #print("For tB =", tB, "The average is:", sum(newlist)/len(newlist))
    return sum(newlist)/len(newlist)
testing_K = []
for x in range(4):
    testing_K.append(0.048+0.0002*x)

with open ("MoreNarrowedK.csv","w", newline = "") as file:
    csvfile = csv.writer(file)
    for K in testing_K:
        row = []
        for tB in range(845,851):
            row.append(round(avgLS(tB,K),3))
        csvfile.writerow(row)
        print("row added!")