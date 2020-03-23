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

def o4(x,y,yaxis):
    colors = (0,0,0)
    area = np.pi*3

    plt.scatter(x,y, s=area, c=colors, alpha=0.5)
    plt.title('scatterplot of ' + yaxis + ' v. Time (using index)')
    plt.xlabel("time (index)")
    plt.ylabel(yaxis)
    plt.show()


def main():
    
    df = pd.read_csv("datamonth.csv", sep = ',')
    
    print("====================")
    print("Keymap: nosubsript: geological spot" + '\n' +
            "subscript = n: magnetic spot" + '\n' +
            "subscript = d: magnetic pole")
    print("====================")
    option = input("Enter 1 for a scatterplot of Theta (geo. spot) v. Theta (mag. pole)" + '\n' +
            "Enter 2 for a scatterplot of Theta (mag. spot) v. Theta (mag. pole)" + '\n' +
            "Enter 3 for a scatterplot of Phi (mag. spot) v. Theta (mag. pole)" + '\n' + 
	                "4 for td v time" + '\n' +
			"5 for tn v time" + '\n' +
			"6 for t v time" + '\n' + 
			"7 for pd v time" + '\n' +
			"8 for pn v time" + '\n' +
			"9 for p v time" + '\n' + 
                        "====================" + '\n')

    if(option == "1"):
        o1(df.td2,df.t)
    if(option == "2"):
        o2(df.td2,df.tn)
    if(option =="3"):
        o3(df.td2,df.pn)
    if(option == "4"):
        o4(df.indx,df.td2,"thetaD")
    if(option == "5"):
        o4(df.indx,df.tn,"thetaN")
    if(option =="6"):
        o4(df.indx,df.t,"theta")
    if(option == "7"):
        o4(df.indx,df.pd2,"phiD")
    if(option == "8"):
        o4(df.indx,df.pn,"phiN")
    if(option =="9"):
        o4(df.indx,df.p,"phi")

if __name__ == "__main__":
    main()
