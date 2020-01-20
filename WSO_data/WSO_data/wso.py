import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import csv
import re

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

def valueExtracter(inFile, carrNum):
    #Gets only the rows that include the neccessaey WSO coefficients
    with open(inFile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(inFile, 'w') as fout:
        fout.writelines(data[14:16])

    file = open(inFile,"r")

    fileLines = file.readlines()

    with open(inFile, "a") as myfile:
        myfile.write(lineToCSVRow(fileLines[0]) + "\n")
        myfile.write(lineToCSVRow(fileLines[1]) + "\n")

    myfile.close()
    file.close()

    #remove the first 2 lines of the text file
    with open(inFile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(inFile, 'w') as fout:
        fout.writelines(data[2:])

    df2 = pd.read_csv(inFile, sep=",", header=None)

    #Add data to coefficent dataframe
    g10 = str(df2.iloc[0,2]) + ","
    g11 = str(df2.iloc[1,2]) + ","
    h11 = str(df2.iloc[1,3])

    coefList = [carrNum, g10, g11, h11]
    print(coefList)

    #adds the coefficents and carrington number to a txt file
    MyFile=open('output.txt','a')

    for element in coefList:
        MyFile.write(element)
    
    MyFile.write('\n')
    MyFile.close()


def main():
    i = 1642
    maxNum = 2215
    while(i <= maxNum):
        carrNum = str(i) + ","
        inputFile = str(i) + ".txt"
        valueExtracter(inputFile, carrNum)
        print(i)
        if(i == maxNum):
            break
        if(i < maxNum):
            i = i+1
    print("all files analyzed.")

if __name__ == "__main__":
    main()
