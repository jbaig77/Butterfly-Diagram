import pandas as pd
import csv
import re

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

def lineToCSVRow(string):
    string = string.strip()
    string2 = list(string)
    i = 0
    while(i < len(string2)):
        if(string2[i] == " " and string2[i-1] != ","):
            string2[i] = ","
        if(string2[i] == " " and string2[i-1 == ","]):
            string2.pop(i)
        i = i+1

    string3 = listToString(string2)
    string3 = string3.replace(" ", "")

    string4 = list(string3)
    j = 1
    while(j < len(string4)):
        if(string4[j] == "," and string4[j-1] == ","):
            string4.pop(j-1)
        j = j+1
    k = 1
    string5 = list(string4)
    while(k < len(string5)):
        if(string5[k] == "," and string5[k-1] == ","):
            string5.pop(k-1)
        k = k+1
    string6 = listToString(string5)
    return string6

def getCarringtonNumber(filename):
    carringtonNumber = filename[:-4]
    return carringtonNumber


def getCoefficents(carringtonNumber, inputFile):

    #Gets only the rows that include the neccessary WSO coefficents
    with open(inputFile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(inputFile, 'w') as fout:
        fout.writelines(data[14:16])
    
    file = open(inputFile,"r")

    fileLines = file.readlines()

    with open(inputFile, "a") as myfile:
        myfile.write(lineToCSVRow(fileLines[0]) + "\n")
        myfile.write(lineToCSVRow(fileLines[1]) + "\n")

    myfile.close()
    file.close()

    #open coefficent csv datafrane
    df = pd.read_csv("wsoCoefficents.csv")

    #remove the first 2 lines of the text file
    with open(inputFile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(inputFile, 'w') as fout:
        fout.writelines(data[2:])

    df2 = pd.read_csv(inputFile, sep=",", header = None)

    #gets the coefficents based on their index
    g10 = df2.iloc[0,2]
    g11 = df2.iloc[1,2]
    h11 = df2.iloc[1,3]

    coefList = [carringtonNumber, g10, g11, h11]

    #adds coefficents to the csv
    for counts in [coefList]:
        df.loc[len(df), :] = counts

    df.to_csv("wsoCoefficents.csv",mode = 'a',index=False,header = None)


def main():

    #add a loop that goes from 1642 to 2215 getting the 
    #carrington number and coefficents from each file 
    #and adding them to a csv.

    i = 1642
    maxNum = 1645
    while(i <= maxNum):
        inputFile = str(i) + ".txt"
        carringtonNumber = getCarringtonNumber(inputFile)
        getCoefficents(carringtonNumber, inputFile)
        print(carringtonNumber + " " + inputFile)
        if(i == maxNum):
            break
        if(i < maxNum):
            i = i+1
    print("All files have been analyzed.")

if __name__ == "__main__":
    main()
