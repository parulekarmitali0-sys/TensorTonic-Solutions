import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    c=x-np.mean(x)
    a=np.sum(c**2)/(len(x)-1)
    d={"variance": float(a), "standard_deviation": float(a**0.5)}
    return d