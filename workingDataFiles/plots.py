import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def o1(x,y):
    colors = (0,0,0)
    area = np.pi*3

    plt.scatter(x,y, s=area, c=colors, alpha=0.5)
    plt.title('scatterplot of Theta (geo. spot) v. Theta (mag. pole)')
    plt.xlabel("Theta (mag. pole)")
    plt.ylabel("Theta (geo.spot)")
    plt.show()

def o2(x,y):
    colors = (0,0,0)
    area = np.pi*3

    plt.scatter(x,y, s=area, c=colors, alpha=0.5)
    plt.title('scatterplot of Theta (mag. spot) v. Theta (mag. pole)')
    plt.xlabel("Theta (mag. pole)")
    plt.ylabel("Theta (mag. spot)")
    plt.show()

def o3(x,y):
    colors = (0,0,0)
    area = np.pi*3

    plt.scatter(x,y, s=area, c=colors, alpha=0.5)
    plt.title('scatterplot of Phi (mag. spot) v. Theta (mag. pole)')
    plt.xlabel("Theta (mag. pole)")
    plt.ylabel("PhiN (mag. spot)")
    plt.show()

def main():
    
    df = pd.read_csv("data.csv", sep = ',')

    option = input("Enter 1 for a scatterplot of Theta (geo. spot) v. Theta (mag. pole)" + '\n' +
            "Enter 2 for a scatterplot of Theta (mag. spot) v. Theta (mag. pole)" + '\n' +
            "Enter 3 for a scatterplot of Phi (mag. spot) v. Theta (mag. pole)" + '\n')

    if(option == "1"):
        o1(df.ThetaD,df.Theta)
    if(option == "2"):
        o2(df.ThetaD,df.ThetaN)
    if(option =="3"):
        o3(df.ThetaD,df.PhiN)

if __name__ == "__main__":
    main()
