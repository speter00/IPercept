import pandas as pd
from scipy.signal import argrelextrema

from read_files import read_data
import utilities as ut
from matplotlib import pyplot as plt

from scipy.signal import savgol_filter
from FFT import plot_fft

import numpy as np

data: pd.Series = read_data()
data = ut.interpolate_outliers(data)

# smoothing the data
# Note: could experiment with different filtering methods, with different parameters

data[:] = savgol_filter(data, 55, 3)

plot_fft(
    data)  # plotting the FFT of the time series, note: data covers roughly 260 minutes, plotting with 10 minute units

# condense the series into data points for every 10 minutes
# in order to make the plot later clearer and more easily understandable

condensed_series = data.groupby(pd.Grouper(freq='10Min')).aggregate(np.mean)


peaks = condensed_series[argrelextrema(condensed_series.values, np.greater)[0]]
# Note: these peaks are also clearly visible on the acceleration_10min plot later

peaks.to_excel("peaks.xlsx") # saving to Excel

summary = dict()

min_acc = data.min()
max_acc = data.max()
avg_acc = data.mean()
median_acc = data.median()
std_acc = data.std()

summary["min"] = min_acc
summary["max"] = max_acc
summary["avg"] = avg_acc
summary["median"] = median_acc
summary["std"] = std_acc

plt.figure(figsize=(20, 20))
plt.plot(condensed_series)

# You can see some interestings bits of information here, such as:
# the machine's acceleration was sharply decreasing overall during the first ~30 minutes (though it did come back up slightly towards the end)
# the machine's acceleration was very low, almost zero around 8:30 for a while
# ...it was also very low not long before 10:30
# the machine's acceleration was peaking around 9:30, although the initial acceleration (at 7:00) was still much higher
# there was another peak at around 11:00

plt.savefig("acceleration_10min_average.png")
pd.DataFrame(data=summary, index=[0]).to_excel("report.xlsx")
