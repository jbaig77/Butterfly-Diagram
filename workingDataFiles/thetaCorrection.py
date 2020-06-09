import pandas as pd
import math
import numpy as np

def main():
    df = pd.read_csv("datamonth.csv", sep = ',')
    N = len(df)
    
    
    for i in range(0,N):
        if(df.t[i] > 180):
            df.tc[i] = 360 - df.t[i]
        else:
            df.tc[i] = df.t[i]
    df.to_csv("datamonth.csv", index = False)
    
if __name__ == "__main__":
    main()
