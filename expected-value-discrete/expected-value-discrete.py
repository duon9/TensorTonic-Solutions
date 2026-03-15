import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    if np.sum(p) != 1:
        raise ValueError
    return x @ p
    
