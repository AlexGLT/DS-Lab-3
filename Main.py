import Array
import DataFrame

DF = DataFrame.dfCreate()
ARR = Array.arrCreate(DF)

struct = {"a": Array, "d": DataFrame}

arrFunc = {"1": Array.overPower, "2": Array.overVoltage, "3": Array.overAmperage,
           "4": Array.randomMean, "5": Array.timeMean}

dfFunc = {"1": DataFrame.overPower, "2": DataFrame.overVoltage, "3": DataFrame.overAmperage,
          "4": DataFrame.randomMean, "5": DataFrame.timeMean}


def funcCall(choice1, choice2):
    if (choice1 == "a"):
        arrFunc[choice2](ARR)

    if (choice1 == "d"):
        dfFunc[choice2](DF)


while (True):
    print("Array (a) or DataFrame (d)?")

    choice1 = input()

    print("1. overPower")
    print("2. overVoltage")
    print("3. overAmperage")
    print("4. randomMean")
    print("5. timeMean")

    choice2 = input()

    funcCall(choice1, choice2)
