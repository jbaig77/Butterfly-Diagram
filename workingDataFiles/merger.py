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

    N = len(dfFinalData)
    M = len(dfCarrington)

    '''
    #algorithm for assigning the correct carrington number to each date
    current = 1
    for j in range(0,N):
        if(dfFinalData.DateInt[j] < dfCarrington.DateInt[current]):
            dfFinalData.Rotation[j] = dfCarrington.Rotation[current-1]
        else:
            while(dfFinalData.DateInt[j] >= dfCarrington.DateInt[current]):
                current = current + 1
            dfFinalData.Rotation[j] = dfCarrington.Rotation[current-1]
        print(str(j))

    dfFinalData.to_csv("finaldata.csv",index=False)
    '''
    #dfCarrington.to_csv("carrington.csv",index=False)

    c = 0
    for j in range(161587,N):
        if(dfFinalData.Rotation[j] == dfThetaNPhiN.Rotation[c]):
            dfFinalData.ThetaN[j] = dfThetaNPhiN.ThetaN[c]
            dfFinalData.PhiN[j] = dfThetaNPhiN.PhiN[c]
        else:
            c = c+1
            
        print(str(j))    

    dfFinalData.to_csv("finaldata.csv", index=False)

if __name__ == "__main__":
    main()
