import pandas as pd
import numpy as np
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

while(True):
    print("Array (a) or DataFrame (d)?")

    choice1 = input()

    print("1. overPower")
    print("2. overVoltage")
    print("3. overAmperage")
    print("4. randomMean")
    print("5. timeMean")

    choice2 = input()

    funcCall(choice1, choice2)
#
#
#
# while(True):
#     print("Array or DataFrame?")
#     choice = input()
#
#     if(choice == "1"):
#         print("1. overPower")
#         print("2. overVoltage")
#         print("3. overAmperage")
#         print("4. randomMean")
#         print("5. timeMean")
#         print("6. periodCombination")
#         choice = input()
#         if(choice == "1"):
#             Array.overPower(ARR)
#
#         if (choice == "2"):
#             Array.overVoltage(ARR)
#
#         if (choice == "3"):
#             Array.overAmperage(ARR)
#
#         if (choice == "4"):
#             Array.randomMean(ARR)
#
#         if (choice == "5"):
#             Array.timeMean(ARR)
#
#         # if (choice == "6"):
#         #     Array.periodCombination(ARR)
#
#     if(choice == "2"):
#         print("1. overPower")
#         print("2. overVoltage")
#         print("3. overAmperage")
#         print("4. randomMean")
#         print("5. timeMean")
#         choice = input()
#         if (choice == "1"):
#             DataFrame.overPower(DF)
#
#         if (choice == "2"):
#             DataFrame.overVoltage(DF)
#
#         if (choice == "3"):
#             DataFrame.overAmperage(DF)
#
#         if (choice == "4"):
#             DataFrame.randomMean(DF)
#
#         if (choice == "5"):
#             DataFrame.timeMean(DF)
#
#         if (choice == "6"):
#             DataFrame.periodCombination(DF)
#
#
# DataFrame.periodCombination(DF)