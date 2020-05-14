import numpy as np
import pandas as pd
import timeit


def arrCreate(DF):
    arr = np.array(DF)

    return arr


def overPower(arr):
    start = timeit.default_timer()

    powerArr = arr[(arr[:, 1]) > 5.0]

    print("Count of raws = {}".format(powerArr.shape[0]))

    print("DateTime GAP GRP Voltage GI sub1 sub2 sub3")
    print(powerArr)
    print("Count of raws = {}".format(powerArr.shape[0]))

    print("Tte execution time = {} seconds".format(timeit.default_timer() - start))


def overVoltage(arr):
    start = timeit.default_timer()

    voltageArr = arr[arr[:, 3] > 235.0]

    print("DateTime GAP GRP Voltage GI sub1 sub2 sub3")
    print(voltageArr)
    print("Count of raws = {}".format(voltageArr.shape[0]))

    print("Tte execution time = {} seconds".format(timeit.default_timer() - start))


def overAmperage(arr):
    start = timeit.default_timer()

    amperageArr = arr[(((arr[:, 1]) * 1000) / arr[:, 3] > 19) & (((arr[:, 1]) * 1000) / arr[:, 3] < 20)]

    print("DateTime GAP GRP Voltage GI sub1 sub2 sub3")
    print(amperageArr)
    print("Count of raws = {}".format(amperageArr.shape[0]))

    print("The execution time = {} seconds".format(timeit.default_timer() - start))


def randomMean(arr):
    start = timeit.default_timer()

    idx = np.random.randint(np.size(arr, 0) - 1, size=500000)

    randomArr = arr[idx, :]

    print("Average for kitchen = {}".format(randomArr[:, 5].mean()))
    print("Average for bathroom = {}".format(randomArr[:, 6].mean()))
    print("Average for room = {}".format(randomArr[:, 7].mean()))

    print("The execution time = {} seconds".format(timeit.default_timer() - start))


def timeMean(arr):
    start = timeit.default_timer()

    firstPart = arr[(pd.to_datetime(arr[:, 0]).hour >= 18) & (arr[:, 1] > 6)]
    print(firstPart)
    print("----------------------")
    firstPart = firstPart[::3, :]
    print(firstPart)
    print("----------------------")

    secondPart = arr[(arr[:, 6] > arr[:, 5]) & (arr[:, 6] > arr[:, 7])]
    print(secondPart)
    print("----------------------")
    secondPart = secondPart[::3, :]
    print(secondPart)
    print("----------------------")

    print("The execution time = {} seconds".format(timeit.default_timer() - start))
