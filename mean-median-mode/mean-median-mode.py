from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    vals, counts = np.unique(x, return_counts = True)
    return {
        'mean' : float(np.mean(x)),
        'median' : float(np.median(x)),
        'mode' : float(vals[np.argmax(counts)]),
    }