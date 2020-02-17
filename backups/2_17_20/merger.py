import pandas as pd
import math

def main():
    dfFinalData = pd.read_csv("finaldata.csv", sep=',')
    dfThetaPhi = pd.read_csv("thetaphi.csv", sep = ',')
    dfCarrington = pd.read_csv("carrington.csv", sep=',')
    dfThetaNPhiN = pd.read_csv("CarringtonNumbersAndCoeff.csv", sep=',')

    #Getting day, month, year, theta, phi from thetaphi.csv
    '''
    dfFinalData['year'] = dfThetaPhi['Year']
    dfFinalData['month'] = dfThetaPhi['Month']
    dfFinalData['day'] = dfThetaPhi['Day']
    dfFinalData['theta'] = dfThetaPhi['Theta']
    dfFinalData['phi'] = dfThetaPhi['Phi']
    '''
    
    #dfFinalData['JD'] = dfFinalData['JD'].astype(float)
    #dfCarrington['JD'] = dfCarrington['JD'].astype(float)

    finaldataRC = dfFinalData.shape[0]
    carringtonRC = dfCarrington.shape[0]

    print(finaldataRC)
    print(carringtonRC)

    N = len(dfFinalData)
    M = len(dfCarrington)


    #algorithm for assigning the correct carrington number to each date

    current = 0
    for(j in range(0,10):
        if(dfFinalData.DateInt[j] < dfCarrington.DateInt[current]):
            dfFinalData.Rotation[j] = dfCarrington.Rotation[current]
        else:
            while(dfFinalData.DateInt[j] >= dfCarrington.DateInt[current]):
                current = current + 1
            dfFinalData.Rotation[j] = dfCarrington.Rotation[current]





    dfFinalData.to_csv("finaldata.csv",index=False)

    #dfCarrington.to_csv("carrington.csv",index=False)

if __name__ == "__main__":
    main()
