import csv
def getCoordinates(i):
    coordinates = ["RTD5010.csv","RTD5011.csv","RTD5012.csv","RTD5013.csv","RTD5014.csv","RTD5015.csv","RTD5021.csv", "RTD5022.csv","RTD5023.csv","RTD5027.csv","RTD5088.csv"]
    xCoords = []
    yCoords = []
    #filename = input("Enter file name (with format extension): ")
    with open(coordinates[i],'r',encoding='utf-8-sig') as file:
        csvfile = csv.reader(file)
        for line in csvfile:
            xCoords.append(float(line[0]))
            yCoords.append(float(line[1]))

    return xCoords, yCoords
            
