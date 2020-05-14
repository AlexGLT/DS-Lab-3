import pandas as pd
import timeit


def dfCreate():
    dataFrame = pd.read_csv("household_power_consumption.txt", parse_dates={"DateTime": [0, 1]}, sep=";",
                            header=1, na_values=["?"]).dropna()
    dataFrame.columns = ["DateTime", "GAP", "GRP", "Voltage", "GI", "sub1", "sub2", "sub3"]

    return dataFrame


def overPower(df):
    start = timeit.default_timer()

    powerdf = df.loc[(df["GAP"]) > 5.0].reset_index().drop("index", axis=1)

    print(powerdf)

    print("The execution time = {} seconds".format(timeit.default_timer() - start))


def overVoltage(df):
    start = timeit.default_timer()

    voltagedf = df.loc[df["Voltage"] > 235.0].reset_index().drop("index", axis=1)

    print(voltagedf)

    print("The execution time = {} seconds".format(timeit.default_timer() - start))


def overAmperage(df):
    start = timeit.default_timer()

    amperagedf = df.loc[((df["GAP"] * 1000) / df["Voltage"] > 19) & ((df["GAP"] * 1000) / df["Voltage"] < 20) &
                        (df["sub2"] > df["sub3"])].reset_index().drop("index", axis=1)

    print(amperagedf)

    print("The execution time = {} seconds".format(timeit.default_timer() - start))


def randomMean(df):
    start = timeit.default_timer()

    sampledf = df.sample(500000).reset_index().drop("index", axis=1)

    print("Average for kitchen = {}".format(sampledf["met"].mean()))
    print("Average for bathroom = {}".format(sampledf["sub2"].mean()))
    print("Average for room = {}".format(sampledf["sub3"].mean()))

    print("The execution time = {} seconds".format(timeit.default_timer() - start))


def timeMean(df):
    start = timeit.default_timer()

    firstPart = df.loc[(df[df.DateTime.dt.hour >= 18]) & (df["GAP"] > 6)]
    print(firstPart)
    print("----------------------")
    firstPart = firstPart[::3, :]
    print(firstPart)
    print("----------------------")

    secondPart = df.loc[(df["sub2"] > df["sub1"]) & (df["sub2"] > df["sub3"])].reset_index().drop("index", axis=1)
    print(secondPart)
    print("----------------------")
    firstPart = secondPart[::4, :]
    print(secondPart)
    print("----------------------")

    print("The execution time = {} seconds".format(timeit.default_timer() - start))
