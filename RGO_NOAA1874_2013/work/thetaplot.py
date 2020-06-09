import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotter(x,y,yaxis):
    colors = (0,0,0)
    area = np.pi * 3

    plt.scatter(x,y, s = area, c = colors, alpha = 0.5)
    plt.title('scatterplot of ' + yaxis + ' v. Time (using index)')
    plt.xlabel("time (index)")
    plt.ylabel(yaxis)
    plt.show()

def main():
    df = pd.read_csv("finaldata.csv", sep = ',')
    plotter(df.indx,df.LatitudeC,"Latitude")

if __name__ == "__main__":
    main()


