from matplotlib import pyplot as plt
import numpy as np
from reader import *
from eulers import *
from optimizer import *

# def plot(i,tB,K):
#     coordinates = ["RTD5010.csv","RTD5011.csv","RTD5012.csv","RTD5013.csv","RTD5014.csv","RTD5015.csv","RTD5021.csv", "RTD5022.csv","RTD5023.csv","RTD5027.csv","RTD5088.csv"]
#     #plotting the points
#     xCoords, yCoords = getCoordinates(i)
#     plt.scatter(xCoords,yCoords)

#     #plotting the function for the model
#     a = findA(xCoords,yCoords,tB,K)
#     xCoordsreal, yCoordsreal, eDict = runEuler(a["aValue"],tB,K)
#     print(a)
#     plt.plot(xCoordsreal,yCoordsreal, "-b", label = "RTD5010")
#     #title = str(coordinates[i])
#     #ax[i//4,i%4].set_title(title, labelsize = 10)
#     return a["leastSquare"]
K = 0.005
tB = 850

# plot(0,tB,K)
plt.title("Ambient Temperature")


# plotting the function for Ta
x = np.linspace(-1100, 2000 ,10000)
y= []
for i in x:
    y.append(f(i,tB,K))
plt.plot(x,y, "-r")
#plt.legend(loc="upper right")
plt.xlabel('Time (Seconds)', fontsize=10)
plt.ylabel('Temperature (Degrees C)', fontsize=10)

plt.xticks([])

plt.yticks([])
plt.show()