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
data, interval=2)  # plotting the FFT of the time series with custom intervals (in minutes)
# Note: higher intervals tend to give smoother graphs, but lower numbers can give a more accurate picture
# I personally found 2 minutes and 5 minutes to work decently well, but fine tuning and experimenting is very much needed


condensed_series = data.groupby(pd.Grouper(freq='5Min')).aggregate(np.mean) # for finding peaks and ploting
# Note: 5 minutes intervals are a bit rough, but peaks in the data are far more visible as a result,
# and the plot is easier to read
# we could however fine tune this simply by reducing the intervals to, for example, 1 minute


condensed_series_1s = data.groupby(pd.Grouper(freq='1s')).aggregate(np.mean) # for finding repeating patterns


# function call below is commented out, because it takes considerable time for it to run; if you wish to run it,
# feel free to remove the comment; the results are in the mfigure files

# ut.matrix_profiler(condensed_series_1s)
# it gives back figures that help determine where to look for repeating patterns
# on figure_1 it clearly shows that the following index-pairs are of interest: 11070-12824, 9458-11212, 11673-13427

# the repeating motifs (three in total) are clearly seen in the pair png files; only a small part of pair1_1 is
# repeated in pair1_2, but pair2 and pair3 both have very similar subsequence pairs

# Note: could look for more motifs... also, the series had to be condensed into 1 second intervals
# because of very high runtime on the original time series; with more time/resources, more accurate analysis could be made


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
# the machine's acceleration somewhat stagnating from around 8:20 to 9:00 roughly
# ...also from around 10:05 to 10:40
# peaks around 10:00 and 9:30 (these are also in the peaks excel file among others), and other peaks
# the machine's acceleration was changing a lot, and very quickly

plt.savefig("acceleration_5min_average.png")
pd.DataFrame(data=summary, index=[0]).to_excel("report.xlsx")
