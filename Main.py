import pandas as pd
import matplotlib.pyplot as plt

import Array
import DataFrame

# DF = DataFrame.dfCreate(0)
# ARR = Array.arrCreate(DF)

arrFunc = {"1": Array.overPower, "2": Array.overVoltage, "3": Array.overAmperage,
           "4": Array.timeMean, "5": Array.randomMean}

dfFunc = {"1": DataFrame.overPower, "2": DataFrame.overVoltage, "3": DataFrame.overAmperage,
          "4": DataFrame.timeMean, "5": DataFrame.randomMean}


def funcCall(choice1, choice2, arr, df):
    if (choice1 == "a"):
        arrFunc[choice2](arr)

    if (choice1 == "d"):
        dfFunc[choice2](df)


def getTime(choice1, choice2, arr, df):
    if (choice1 == "a"):
        time = arrFunc[choice2](arr)

    if (choice1 == "d"):
        time = dfFunc[choice2](df)

    return time


# while (True):
#     print("Array (a) or DataFrame (d)?")
#
#     choice1 = input()
#
#     print("1. overPower")
#     print("2. overVoltage")
#     print("3. overAmperage")
#     print("4. randomMean")
#     print("5. timeMean")
#
#     choice2 = input()
#
#     funcCall(choice1, choice2)

arrOverPowerTime = []
arrOverVoltageTime = []
arrOverAmperageTime = []
arrTimeMeanTime = []

dfOverPowerTime = []
dfOverVoltageTime = []
dfOverAmperageTime = []
dfTimeMeanTime = []

Pandas = [arrOverPowerTime, arrOverVoltageTime, arrOverAmperageTime, arrTimeMeanTime]
Numpy = [dfOverPowerTime, dfOverVoltageTime, dfOverAmperageTime, dfTimeMeanTime]

for i in range(1, 7):
    df = DataFrame.dfCreate(pow(10, i))
    arr = Array.arrCreate(df)

    for j in range(1, 5):
        timea = getTime("a", "{}".format(j), arr, df)
        print(timea)
        Numpy[j - 1].append(timea)
        timed = getTime("d", "{}".format(j), arr, df)
        Pandas[j - 1].append(timed)

count = ["10", "100", "1000", "10000", "100000", "1000000"]

overPowerTable = pd.DataFrame({"Array": Numpy[0], "DataFrame": Pandas[0],
            "Count": count}).set_index("Count")
overVoltageTable = pd.DataFrame({"Array": Numpy[1], "DataFrame": Pandas[1],
            "Count": count}).set_index("Count")
overAmperageTable = pd.DataFrame({"Array": Numpy[2], "DataFrame": Pandas[2],
            "Count": count}).set_index("Count")
timeMeanTable = pd.DataFrame({"Array": Numpy[3], "DataFrame": Pandas[3],
            "Count": count}).set_index("Count")

overPowerPlot = overPowerTable.plot(title="Over Power", grid=True)
overVoltagePlot = overVoltageTable.plot(title="Over Voltage", grid=True)
overAmperagePlot = overAmperageTable.plot(title="Over Amperage", grid=True)
timeMeanPlot = timeMeanTable.plot(title="Time Mean", grid=True)

plt.show()
