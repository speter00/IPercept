import pandas as pd


def read_data():
    # it's best to use the date-time column as an index column

    data1 = pd.read_csv("test_files/spacedata1.csv", index_col=0, header=None).squeeze("columns")
    data2 = pd.read_csv("test_files/spacedata2.csv", index_col=0, header=None).squeeze("columns")
    data3 = pd.read_csv("test_files/spacedata3.csv", index_col=0, header=None).squeeze("columns")
    data4 = pd.read_csv("test_files/spacedata4.csv", index_col=0, header=None).squeeze("columns")

    # this one (data5) contains some malformed rows with wrong separators
    # a solution for this is to accept semicolons, commas and left arrows as separators, multiple if necessary

    data5 = pd.read_csv("test_files/spacedata5.csv", sep=r'[;,<]+', names=["Date_Time","Acceleration"])

    data1.index = pd.to_datetime(data1.index)
    data2.index = pd.to_datetime(data2.index)
    data3.index = pd.to_datetime(data3.index)
    data4.index = pd.to_datetime(data4.index)

    # Forward fill missing timestamps

    data5 = data5.set_index(pd.to_datetime(data5["Date_Time"].fillna(method="ffill")))["Acceleration"]

    # Interpolating to fill in missing values
    data1 = data1.interpolate(method="time")
    data2 = data2.interpolate(method="time")
    data3 = data3.interpolate(method="time")
    data4 = data4.interpolate(method="time")
    data5 = data5.interpolate(method="time")

    return pd.concat([data1, data2, data3, data4, data5], axis=0)