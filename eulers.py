import csv
import math
import numpy as np

#possible things to change: Tb (in the if condition) and the temp decay value (in the else)

def f(x,tB,K):
    if x < -tB:
        return 23
    elif x < 0:
        return 540
    else:
        return 517 * math.exp(-K * x) + 23
        #BEST VALUE SO FAR: -0.00616 for this temp decay thing

def derivative(x,y,a,tB,K):
    return a * (f(x,tB,K) - y)

def runEuler(a,tB,K):
    x0 = -tB - 10
    y0 = 23
    x = [x0]
    y = [y0]
    dicX = dict()
    iterations = 45500
    stepsize = 0.1
    for i in range(iterations):
        x.append(round(x[i] + stepsize, 8))
        y.append(y[i] + derivative(x[i],y[i],a,tB,K) * stepsize)
        dicX[x[i+1]] = y[i+1]

    return x,y,dicX


if __name__ == "__main__":
    with open('e.csv', 'w', newline = '') as file:
        writer = csv.writer(file)


        header = ["x","y"]#write header here
        writer.writerow(header)

        current_point = [0,1] #starting point here
        step = 0.25#write step size here
        writer.writerow(current_point)

        iterations = 80#write # of iterations here

        for i in range(iterations):
            x = current_point[0]
            y = current_point[1]
            current_point[0] += step
            current_point[1] += step * derivative(y)


        
            #true = f(current_point[0])
            #error = true - current_point[1]

            
            writer.writerow(current_point)