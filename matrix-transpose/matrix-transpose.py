import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    arr = A.copy()
    n, m = len(arr), len(arr[0])
    arr_fake = [[0] * n for i in range(m)]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j], arr_fake[j][i] = arr_fake[j][i], arr[i][j]
            
            
    return np.array(arr_fake)
