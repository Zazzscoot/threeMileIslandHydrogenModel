from matplotlib import pyplot as plt
import numpy as np
from reader import *
from eulers import *
from optimizer import *

def plot(i,tB,K):
    coordinates = ["RTD5010.csv","RTD5011.csv","RTD5012.csv","RTD5013.csv","RTD5014.csv","RTD5015.csv","RTD5021.csv", "RTD5022.csv","RTD5023.csv","RTD5027.csv","RTD5088.csv"]
    #plotting the points
    xCoords, yCoords = getCoordinates(i)
    ax[i//4,i%4].scatter(xCoords,yCoords)

    #plotting the function for the model
    a = findA(xCoords,yCoords,tB,K)
    xCoordsreal, yCoordsreal, eDict = runEuler(a["aValue"],tB,K)
    print(a)
    ax[i//4,i%4].plot(xCoordsreal,yCoordsreal)
    title = str(coordinates[i][:-4])
    ax[i//4,i%4].set_title(title)
    return a["leastSquare"]

fig,ax = plt.subplots(3,4)
newlist = []
tB = 1100
K = 100
for i in range(0,11):
    newlist.append(plot(i,tB,K))

ax[2,3].axis("off")

fig.suptitle("Tb = " + str(tB) + " K = " + str(K) + " Sum of Least Squares = " + str(round(sum(newlist),3)))

# plotting the function for Ta
# x = np.linspace(-800, 3299, 100000)
# y= []
# for i in x:
#     y.append(f(i))
# plt.plot(x,y)

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
plt.show()