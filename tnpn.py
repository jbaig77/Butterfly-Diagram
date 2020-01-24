import pandas as pd
import numpy as np
import math

def Bo(g10, g11, h11):
    b = np.sqrt(math.pow(g10, 2) + math.pow(g11, 2) + math.pow(h11, 2))
    return b

def thetaN(g10, b):
    return thetaN

def phiN(g11,h11):
    return phiN

def main():
    file = "CarringtonNumbersAndCoeff.csv"
    df = pd.read_csv(file, sep=",")
    #Calculates Bo, the square root of the sum of the squares of the WSO coefficents
    df['Bo'] = ((df['g10'] ** 2) + (df['g11'] ** 2) + (df['h11'] ** 2)) ** (1/2)


    df['thetaN'] = np.degrees(np.arccos(df['g10'].astype(float)/df['Bo'].astype(float)))

    df['phiN'] = np.degrees(np.arctan2(df['h11'].astype(float), df['g11'].astype(float)))

    df.to_csv(file,index=False)

    print(np.degrees(np.arccos(-29.95/86.56)))

if __name__ == "__main__":
    main()