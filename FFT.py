import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def plot_fft(data: pd.Series):
    """
    Plot the Fast Fourier Transformed version of the input data. Plotting with 10 minute units.
    It's a slightly modified version of this code:
    https://towardsdatascience.com/fourier-transform-for-time-series-292eb887b101
    :param data: The input time series.
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
    results['period'] = results['freq'] * 26  # the data covers approx. 260 minutes in total, and the units are 10 minutes
    results['period_round'] = results['period'].round()
    grouped_10mins = results.groupby('period_round')['nspectrum'].sum()
    plt.semilogy(grouped_10mins.index, grouped_10mins)
    plt.savefig("fft_acceleration_10min.png")