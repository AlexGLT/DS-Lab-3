import pandas as pd
from datetime import datetime

def dfCreate():
    dataFrame = pd.read_csv("household_power_consumption.txt", parse_dates={"DateTime": [0, 1]}, sep=";",
                            header=300000, na_values=["?"]).dropna()
    dataFrame.columns = ["DateTime", "GAP", "GRP", "Voltage", "GI", "met1", "met2", "met3"]

    return dataFrame

def overPower(df):
    start_time = datetime.now()

    powerdf = df.loc[(df["GAP"] + df["GRP"]) > 5.0].reset_index().drop("index", axis=1)

    end_time = datetime.now()

    print(powerdf)

    print("The execution time = {}".format(end_time - start_time))

def overVoltage(df):
    start_time = datetime.now()

    voltagedf = df.loc[df["Voltage"] > 235.0].reset_index().drop("index", axis=1)

    end_time = datetime.now()

    print(voltagedf)

    print("The execution time = {}".format(end_time - start_time))

def overAmperage(df):
    start_time = datetime.now()

    amperagedf = df.loc[((df["GAP"]*1000)/df["Voltage"] > 19) & ((df["GAP"]*1000)/df["Voltage"] < 20) & (df["met2"] > df["met3"])].reset_index().drop("index", axis=1)

    end_time = datetime.now()

    print(amperagedf)

    print("The execution time = {}".format(end_time - start_time))

def randomMean(df):
    start_time = datetime.now()

    sampledf = df.sample(500000).reset_index().drop("index", axis=1)

    end_time = datetime.now()

    print("Average for kitchen = {}".format(sampledf["met"].mean()))
    print("Average for bathroom = {}".format(sampledf["met2"].mean()))
    print("Average for room = {}".format(sampledf["met3"].mean()))

    print("The execution time = {}".format(end_time - start_time))

def timeMean(df):
    start_time = datetime.now()

    df = df.loc[(df[df.DateTime.dt.hour >= 18]) & ((df["GAP"] + df.loc["GRP"]) > 6)]
    df = df.loc[(df["met2"] > df["met1"]) & (df["met2"] > df["met3"])].reset_index().drop("index", axis=1)

    end_time = datetime.now()

    print(df)

    print("The execution time = {}".format(end_time - start_time))

def periodCombination(df):
    maxMetDat = df.loc[(df["DateTime"].dt.year == 2009) & (df["DateTime"].dt.month == 3) & (df["DateTime"].dt.day == 22)].reset_index().drop("index", axis=1)

    print(maxMetDat)

    print(maxMetDat.GAP.idxmin())

    a = maxMetDat.GAP.idxmin()

    print(maxMetDat.iloc[a])
