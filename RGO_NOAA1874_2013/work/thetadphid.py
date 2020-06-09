import pandas as pd
import math
import numpy as np

def ThetaD(theta,phi,thetaN,phiN):
    thetad2 = np.degrees(np.arccos(((np.cos(thetaN)*np.cos(theta)) +
        (np.sin(thetaN)*np.sin(theta)*np.cos(phi - phiN)))))
    return thetad2
    

def PhiD(theta, thetaN, thetaD, phi, phiN):
    phid2 = np.degrees(np.arcsin((np.sin(theta)*np.sin(phi-phiN)) / np.sin(thetaD)))
    return phid2


def main():
    dfD = pd.read_csv("finaldata.csv", sep = ',')
    N = len(dfD)

    for j in range(0,N):
        dfD.td[j] = ThetaD(dfD.tc[j], dfD.p[j], dfD.tn[j], dfD.pn[j])

    dfD.to_csv("finaldata.csv", index = False)
    '''
    for k in range(0,N):
        dfD.pd[k] = PhiD(dfD.tc[k], dfD.tn[k], dfD.td[k], dfD.p[k], dfD.pn[k])
    
    dfD.to_csv("finaldata.csv", index = False)
    '''
if __name__ == "__main__":
    main()
