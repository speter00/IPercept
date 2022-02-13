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






