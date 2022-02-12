import pandas as pd
import utilities as ut


data1 = pd.read_csv("test_files/spacedata1.csv", header=None)
data2 = pd.read_csv("test_files/spacedata2.csv", header=None)
data3 = pd.read_csv("test_files/spacedata3.csv", header=None)
data4 = pd.read_csv("test_files/spacedata4.csv", header=None)

# this one contains some malformed rows with wrong separators
# a solution for this is to accept semicolons, commas and left arrows as separators, multiple if necessary

data5 = pd.read_csv("test_files/spacedata5.csv", sep=r'[;,<]+', header=None)

# In order to make later operations simplier and cleaner,
# it's best to separate the first columns (date-time) into 2 date, time columns

data1 = ut.tidy_columns(data1)
data2 = ut.tidy_columns(data2)
data3 = ut.tidy_columns(data3)
data4 = ut.tidy_columns(data4)
data5 = ut.tidy_columns(data5)




