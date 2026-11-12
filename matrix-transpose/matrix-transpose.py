import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    a1=len(A[0])
    a2=len(A)
    a=np.empty((a1,a2))
    for i in range(a2):
        for j in range(a1):
            a[j][i]=A[i][j]
    return a
