import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#This function returns the line number of a file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#This function calculates the average of a list
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

def dataRetrever(inputFile,outputFile):
    file1 = open(inputFile,"r")
    file2 = open(outputFile,"w")

    file1Lines = file1.readlines()

    lineNumber = file_len(inputFile)

    #This while loop organizes the data into a useable format
    i = 0
    while(i < lineNumber):
        line = file1Lines[i]
        year = int(line[0:4])
        month = int(line[4:6])
        day = int(line[6:8])
        theta = float(line[51:56])
        phi = float(line[57:62])
        lat = float(line[63:68])
        file2.write(str(year)+","+str(month)+","+str(day)+","+str(theta)+","+str(phi)+","+str(lat)+"\n")
        i = i + 1

    file1.close()
    file2.close()

    #Opening the csv and adding the appropriate column names
    df = pd.read_csv(outputFile, 
                        sep=',',
                        names=["Year","Month","Day","Theta","Phi","Latitude"])

    df.to_csv(outputFile, index=False)

def main():
    i = 1874
    maxYear = 2013
    while(i <= 2013):
        inputFile = "g" + str(i) + ".txt"
        csvFilename = inputFile[:-4]
        outputFile = csvFilename + ".csv"
        dataRetrever(inputFile, outputFile)
        if(i == maxYear):
            break
        if(i < maxYear):
            i = i+1
    print("All text files have been converted.")
      
if __name__ == "__main__":
    main()
