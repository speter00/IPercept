import pandas as pd
from read_files import read_data
from scipy import stats

data: pd.Series = read_data()
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

zscores = stats.zscore(data)
outliers = data[zscores[abs(zscores) > 3].index]

print("Outliers are: ", outliers)


