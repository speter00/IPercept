from typing import List, Tuple

import pandas as pd
from scipy import stats
from scipy.signal import argrelextrema
import numpy as np

def interpolate_outliers(data: pd.Series) -> pd.Series:
    """
    Interpolate outlier values in the data.

    :param data: The input data.
    :return: Data with interpolated values.
    """

    # Mask outlier values with nan, then pass them on for interpolation

    zscores = stats.zscore(data)
    outliers = data[zscores[abs(zscores) > 3].index]  # both negative and positive outliers matter (thus the abs)
    return data.mask(data.isin(outliers)).interpolate(method="time")

def peak_finder(data: pd.Series) -> pd.Series:
    '''
    Function for finding peaks in acceleration.

    :param data: Input data.
    :return: Peak accelerations with timestamps.
    '''

    # Note: local minimums are not low enough to have a high enough absolute Z-Score,
    # but decreasing Z-Score threshold gives too many peaks. Some fine tuning could be needed.

    zscores = stats.zscore(data)
    extreme_zscores = zscores[abs(zscores) > 2]
    ex_z_loc_maximums = extreme_zscores[argrelextrema(extreme_zscores.values, np.greater)[0]] # local maximums for extreme z-scores
    max_peaks = data[ex_z_loc_maximums.index] # data, where timestamp matches that of a local max's timestamp
    return max_peaks
