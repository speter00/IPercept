import pandas as pd
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pickle

def train_model(data: pd.Series):
    '''
    Function for training a model that predicts future acceleration values based on past values.

    :param data: The input time series of acceleration values.
    '''
    target_values = []
    features = []

    t = data.index.min() + relativedelta(hours=4) # jumping 4 hours ahead from the beginning, to 11:00
    while t < data.index.max():
        target_values.append(data[t:t])

        known = data.loc[t - relativedelta(minutes=30): t - relativedelta(seconds=0.1)] # make the past 30 minutes known
        features.append(known.tolist())

        t = t + relativedelta(seconds=0.1) # move the time window by 0.1 seconds

    train_features = features[:int(len(features)*0.9)]      #90% - 10% train-test split
    test_features = features[int(len(features)*0.9):]
    train_labels = target_values[:int(len(target_values)*0.9)]
    test_labels = target_values[int(len(target_values)*0.9):]


    # Note: Using a DecisionTreeRegressor isn't necessarily the best option, other options with different parameters
    # should be tried; different prediction methods could also be attempted, such as ARIMA
    dt = DecisionTreeRegressor()
    dt.fit(train_features, train_labels)
    prediction = dt.predict(test_features)

    print("Error: ", mean_squared_error(prediction, test_labels))

    # since training takes a long time,
    # the model should be saved to avoid having to re-train

    # it's also useful to save other data in order to plot them later for visualizing performance


    pickle.dump(dt, open("model.p", "wb"))
    pickle.dump(prediction, open("prediction.p", "wb"))
    pickle.dump(test_labels, open("test_labels.p", "wb"))
    pickle.dump(train_labels, open("train_labels.p", "wb"))


def test_plot():
    '''
    Function for visualizing performance of acceleration predictor model.
    '''
    train_labels = pickle.load(open("train_labels.p", "rb"))
    test_labels = pickle.load(open("test_labels.p", "rb"))
    prediction = pickle.load(open("prediction.p", "rb"))

    fig, ax = plt.subplots(figsize=(120, 10))
    plt.plot(range(0, len(train_labels)), train_labels, c='grey', alpha=0.5)
    testrange = range(len(train_labels) - 1, len(train_labels) + len(test_labels) - 1)
    plt.plot(testrange, test_labels, c='c', marker='o', markersize=1)
    plt.plot(testrange, prediction, c='r', marker='o', alpha=0.7, markersize=1)
    ax.legend(['past', 'future', 'predicted_future'])
    plt.savefig("test_plot.png")