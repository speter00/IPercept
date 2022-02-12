import pandas as pd

def tidy_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    This helper function is for separating the date-time column into separate date and time columns
    and renaming them, keeping the original's "date"-value order.

    :param data: The input dataframe.
    :return: The column-separated dataframe.
    """

    data[["Date", "Time"]] = data[0].str.split(' ', 1, expand=True)
    data = data[["Date", "Time", 1]]
    return data.rename(columns={1: "Acceleration"})