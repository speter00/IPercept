import pandas as pd
import stumpy as stumpy

from read_files import read_data
import utilities as ut
from matplotlib import pyplot as plt

from scipy.signal import savgol_filter

import numpy as np

data: pd.Series = read_data()
data = ut.interpolate_outliers(data)

# smoothing the data
# Note: could experiment with different filtering methods, with different parameters

data[:] = savgol_filter(data, 55, 3)

peaks = ut.peak_finder(data)






# condense the series into data points for every 10 minutes
# in order to make the plot later clearer and more easily understandable

condensed_series = data.groupby(pd.Grouper(freq='10Min')).aggregate(np.mean)



data_index_range = list(range(len(data.index)))
data_fft = abs(np.fft.fft(data))

# get the list of frequencies
num = np.size(data_index_range)
freq = [i / num for i in list(range(num))]

# get the list of spectrums
spectrum=data_fft.real*data_fft.real+data_fft.imag*data_fft.imag
nspectrum=spectrum/spectrum[0]


results = pd.DataFrame({'freq': freq, 'nspectrum': nspectrum})
results['period'] = results['freq'] * 26
results['period_round'] = results['period'].round()
grouped_10mins = results.groupby('period_round')['nspectrum'].mean()
plt.semilogy(grouped_10mins.index, grouped_10mins)
plt.savefig("fft_acceleration_10min.png")

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

plt.figure(figsize=(20,20))
plt.plot(condensed_series)

# You can see some interestings bits of information here, such as:
# the machine's acceleration was sharply decreasing overall during the first ~30 minutes (though it did come back up slightly towards the end)
# the machine's acceleration was very low, almost zero around 8:30 for a while
# ...it was also very low not long before 10:30
# the machine's acceleration was peaking around 9:30, although the initial acceleration (at 7:00) was still much higher
# there was another peak at around 11:00

plt.savefig("acceleration_10min_average.png")



