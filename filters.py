import numpy as np
from scipy.signal import butter, lfilter


def pre_emphasis(signal, alpha=0.97):
    """
    Apply a pre-emphasis filter on the input signal.
    y[n] = x[n] - alpha * x[n-1]
    alpha b/w 0 to 1 
    """
    # The first sample stays the same, the rest are processed
    return np.append(signal[0], signal[1:] - alpha * signal[:-1])


def butter_bandpass(signal,lowcut, highcut, fs, order=4):
    nyquist = 0.5 *fs
    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype='bandstop')
    return lfilter(b, a, signal)



