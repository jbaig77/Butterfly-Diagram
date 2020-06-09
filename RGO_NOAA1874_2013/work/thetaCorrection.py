import pandas as pd
import math
import numpy as np

def main():
    df = pd.read_csv("finaldata.csv", sep = ',')
    N = len(df)
    
    for i in range(0,N):
        df.LatitudeC[i] = 90 - df.Latitude[i]
            
    df.to_csv("finaldata.csv", index = False)
    
if __name__ == "__main__":
    main()
