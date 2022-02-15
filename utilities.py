import matrixprofile as mp

import pandas as pd
from scipy import stats


def interpolate_outliers(data: pd.Series) -> pd.Series:
    """
    Interpolate outlier values in the data.

    :param data: The input data to interpolate.
    :return: Data with interpolated values.
    """

    # Mask outlier values with nan, then pass them on for interpolation

    zscores = stats.zscore(data)
    outliers = data[zscores[abs(zscores) > 3].index]  # both negative and positive outliers matter (thus the abs)
    return data.mask(data.isin(outliers)).interpolate(method="time")




def matrix_profiler(data: pd.Series):
    '''
    Make a matrix profile from the data in order to find repeating patterns.

    :param data: The time series to analyze.
    '''
    mprofile, figures = mp.analyze(data.values)
    for i in range(len(figures)):
        figures[i].savefig(f"mfigure_{i}.png")