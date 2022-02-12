import pandas as pd
import utilities as ut

# In order to make later operations simplier and cleaner,
# it's best to separate the first columns (date-time) into 2 date, time columns

data1 = pd.read_csv("test_files/spacedata1.csv", sep=r'[ ,]', header=None, names=["Date", "Time", "Acceleration"])
data2 = pd.read_csv("test_files/spacedata2.csv", sep=r'[ ,]', header=None, names=["Date", "Time", "Acceleration"])
data3 = pd.read_csv("test_files/spacedata3.csv", sep=r'[ ,]', header=None, names=["Date", "Time", "Acceleration"])
data4 = pd.read_csv("test_files/spacedata4.csv", sep=r'[ ,]', header=None, names=["Date", "Time", "Acceleration"])

# this one contains some malformed rows with wrong separators
# a solution for this is to accept semicolons, commas and left arrows as separators, multiple if necessary

data5 = pd.read_csv("test_files/spacedata5.csv", sep=r'[ ;,<]+', header=None, names=["Date", "Time", "Acceleration"])








