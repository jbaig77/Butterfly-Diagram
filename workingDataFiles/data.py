import pandas as pd
import math
import numpy as np

def ThetaD(theta,phi,thetaN,phiN):
    #thetad = math.acos(((math.cos(thetaN)*math.cos(theta)) + (math.sin(thetaN)*math.sin(theta)*math.cos(phi - phiN))))
    thetad2 = np.degrees(np.arccos(((np.cos(thetaN)*np.cos(theta)) +
        (np.sin(thetaN)*np.sin(theta)*np.cos(phi - phiN)))))

    return thetad2
    

def PhiD(theta, thetaN, thetaD, phi, phiN):
    #phid = math.acos(-((math.cos(theta)-(math.cos(thetaN)*math.cos(thetaD))) / (math.sin(thetaN)*math.sin(thetaD))))
    #phid = math.asin((math.sin(theta)*math.sin(phi-phiN)) / math.sin(thetaD))

    phid2 = np.degrees(np.arcsin((np.sin(theta)*np.sin(phi-phiN)) / np.sin(thetaD)))

    return phid2


def main():
    #dfC = pd.read_csv("CarringtonNumbersAndCoeff.csv", sep = ',')
    dfD = pd.read_csv("data.csv", sep = ',')

    N = len(dfD)
    """
    c = 0
    for j in range(0,N):
        if(dfD.Rotation[j] == dfC.Rotation[c]):
            dfD.ThetaN[j] = dfC.ThetaN[c]
            dfD.PhiN[j] = dfC.PhiN[c]
        else:
            c = c+1
            if(dfD.Rotation[j] == dfC.Rotation[c]):
                dfD.ThetaN[j] = dfC.ThetaN[c]
                dfD.PhiN[j] = dfC.PhiN[c]

        print(str(j))
    """

    for j in range(0,N):
        dfD.ThetaD2[j] = ThetaD(dfD.Theta[j], dfD.Phi[j], dfD.ThetaN[j], dfD.PhiN[j])
        print("j = " + str(j) + " ThetaD[j]: " + str(dfD.ThetaD[j]))

    dfD.to_csv("data.csv", index = False)
    

    for k in range(0,N):
        dfD.PhiD2[k] = PhiD(dfD.Theta[k], dfD.ThetaN[k], dfD.ThetaD[k], dfD.Phi[k], dfD.PhiN[k])
        print("k = ", str(k) + " PhiD[k]: " + str(dfD.PhiD[k]))
    
    dfD.to_csv("data.csv", index = False)

if __name__ == "__main__":
    main()
