import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    _, count = np.unique(y, return_counts = True)

    p = count / sum(count)

    return np.abs(p @ np.log2(p))
