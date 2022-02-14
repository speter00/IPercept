from typing import List, Tuple

import pandas as pd
from scipy import stats
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
