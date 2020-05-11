import numpy as np
import pandas as pd
from datetime import datetime

def arrCreate():
    source = np.genfromtxt("household_power_consumption.txt", delimiter=";", skip_header=1, skip_footer=2075000,
                          names=["Date", "Time", "GAP", "GRP", "Voltage", "GI", "met1", "met2", "met3"],
                          dtype=["U19", "U8", "float32", "float32", "float32", "float32", "float32", "float32", "float32"])

    raws = []

    for i in source:
        datetime = pd.to_datetime(i[0] + ' ' + i[1])

        raw = [datetime, i[2], i[3], i[4], i[5], i[6], i[7], i[8]]

        if(np.isnan(i[3]) | np.isnan(i[4]) | np.isnan(i[5]) | np.isnan(i[6]) | np.isnan(i[7]) | np.isnan(i[8])):
            continue

        raws.append(raw)

    arr = np.array(raws)

    return arr

def overPower(arr):
    start_time = datetime.now()

    powerArr = arr[(arr[:, 1] + arr[:, 2]) > 5.0]

    end_time = datetime.now()

    print("DateTime GAP GRP Voltage GI met1 met2 met3")
    print(powerArr)

    print("The execution time = {}".format(end_time - start_time))

def overVoltage(arr):
    start_time = datetime.now()

    voltageArr = arr[arr[:, 3] > 235.0]

    end_time = datetime.now()

    print("DateTime GAP GRP Voltage GI met1 met2 met3")
    print(voltageArr)

    print("The execution time = {}".format(end_time - start_time))

def overAmperage(arr):
    start_time = datetime.now()

    amperageArr = arr[(((arr[:, 1] + arr[:, 2])*1000)/arr[:, 3] > 19) & (((arr[:, 1] + arr[:, 2])*1000)/arr[:, 3] < 20)]

    end_time = datetime.now()

    print("DateTime GAP GRP Voltage GI met1 met2 met3")
    print(amperageArr)
    print("The execution time = {}".format(end_time - start_time))

def randomMean(arr):
    start_time = datetime.now()

    idx = np.random.randint(np.size(arr, 0) - 1, size=500000)

    end_time = datetime.now()

    randomArr = arr[idx, :]

    print("Average for kitchen = {}".format(randomArr[:, 5].mean()))
    print("Average for bathroom = {}".format(randomArr[:, 6].mean()))
    print("Average for room = {}".format(randomArr[:, 7].mean()))

    print("The execution time = {}".format(end_time - start_time))

def timeMean(arr):
    start_time = datetime.now()

    temp = arr[(pd.to_datetime(arr[:, 0]).hour >= 18) & ((arr[:, 1] + arr[:, 2]) > 6)]

    end_time = datetime.now()

    timeArr = temp[(temp[:, 6] > temp[:, 5]) & (temp[:, 6] > temp[:, 7])]

    print(timeArr)

    print("The execution time = {}".format(end_time - start_time))

# def periodCombination(arr):
#     maxMetDat = arr[(pd.to_datetime(arr[:, 0]).year == 2007) & (pd.to_datetime(arr[:, 0]).month == 3) & (pd.to_datetime(arr[:, 0]).day == 22)]
#
#     print(df.loc[(df["DateTime"].dt.year == 2007) & (df["DateTime"].dt.month == 3) & (df["DateTime"].dt.day == 22)])
#     print(maxMetDat)