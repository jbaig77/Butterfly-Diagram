import pandas as pd
import math
import numpy as np

def avg(lst):
    return sum(lst) / len(lst)

def main():
    
    df = pd.read_csv("data.csv", sep = ',')
    N = len(df)

    dfm = pd.read_csv("datamonth.csv", sep = ',')

    i = 0 #this will keep track of the line number for dfm
    j = 0 #this will keep track of the line number for df
    
    T = []
    P = [] 
    TN = []
    PN = []
    TD = [] 
    PD = []
    TD2 = []
    PD2 = []


    SS = [] #this list will hold the values of the 
            #sunspot coords for each month

    MP = [] #list for MagPolCoords for each month

    row = [] #this row will be added to datamonth.csv

    for j in range(1,N):
        if(df.Month[j] == df.Month[j-1]):
            T.append(df.Theta[j-1])
            P.append(df.Phi[j-1])
            TN.append(df.ThetaN[j-1])
            PN.append(df.PhiN[j-1])
            TD.append(df.ThetaD[j-1])
            PD.append(df.PhiD[j-1])
            TD2.append(df.ThetaD2[j-1])
            PD2.append(df.PhiD2[j-1])

            
        if(df.Month[j] != df.Month[j-1]):   
            #print(*T, sep = ',')
            #print( str(sum(T)) + " " + str(len(T)))
            t = avg(T)
            p = avg(P)
            tn = avg(TN)
            pn = avg(PN)
            td = avg(TD)
            pdd = avg(PD)
            td2 = avg(TD2)
            pd2 = avg(PD2)

            row = [df.Year[j-1],df.Month[j-1],t,p,tn,pn,td,pdd,td2,pd2]
            M = len(dfm)
            dfm.loc[M] = row

            #clear all lists
            T.clear()
            P.clear()
            TN.clear()
            PN.clear()
            TD.clear()
            PD.clear()
            TD2.clear()
            PD2.clear()

            #print(dfm.loc[j])

            dfm.to_csv('datamonth.csv', index = False)
    
    print(dfm.head())



if __name__ == "__main__":
    main()
