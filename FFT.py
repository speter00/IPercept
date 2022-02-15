import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def plot_fft(data: pd.Series, interval=5):
    """
    Plot the Fast Fourier Transformed version of the input data.
    It's a slightly modified version of this code:
    https://towardsdatascience.com/fourier-transform-for-time-series-292eb887b101

    :param data: The input time series.
    :param interval: Plotting with this many units (in minutes).
    """

    data_index_range = list(range(len(data.index)))
    data_fft = abs(np.fft.fft(data))

    # get the list of frequencies
    num = np.size(data_index_range)
    freq = [i / num for i in list(range(num))]

    # get the list of spectrums
    spectrum = data_fft.real * data_fft.real + data_fft.imag * data_fft.imag
    nspectrum = spectrum / spectrum[0]

    results = pd.DataFrame({'freq': freq, 'nspectrum': nspectrum})
    results['period'] = results['freq'] * (260 / interval)  # the data covers approx. 260 minutes in total,
    results['period_round'] = results['period'].round()
    grouped = results.groupby('period_round')['nspectrum'].mean()
    plt.semilogy(grouped.index, grouped)
    plt.savefig(f"fft_acceleration_{interval}min.png")