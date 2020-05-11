import pandas as pd
import numpy as np
import timeit
import Array
import DataFrame

pd.options.display.max_columns = 9
pd.options.display.max_rows = 500

np.set_printoptions(edgeitems=10)

DF = DataFrame.dfCreate()

# ARR = Array.arrCreate()

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


DataFrame.periodCombination(DF)