import csv
import numpy as np

def getDataSource(path):
    sizeofTV=[]
    averageTimeSpent=[]
    with open(path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sizeofTV.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return{"x":sizeofTV,"y":averageTimeSpent}

    
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between size of TV and average time spent watching TV in a week",correlation[0,1])

def setup():
    path="tv.csv"
    datasource=getDataSource(path)
    findcorrelation(datasource)

setup()