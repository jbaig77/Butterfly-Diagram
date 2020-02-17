import pandas as pd
import math


def Format(year, month, day):
    
    if(len(str(month)) == 1):
        month = "0"+str(month)
    if(len(str(day)) == 1):
        day = "0"+str(day)

    output = str(year) + str(month) + str(day)
    return output


def main():
    filename = "finaldata.csv"
    dfCarrington = pd.read_csv(filename, sep=',')

    numbRows = len(dfCarrington)
    print(str(numbRows))

    for i in range(0, numbRows):
        dfCarrington.DateInt[i] = Format(dfCarrington.Year[i],
                                        dfCarrington.Month[i],
                                        dfCarrington.Day[i])
        print(str(i))

    dfCarrington.to_csv(filename,index=False)


if __name__ == "__main__":
    main()
