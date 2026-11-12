from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    d={i: x.count(i) for i in x}
    an=[i for i in x if x.count(i)==max(d.values())]
    
    ans={'mean':float(np.mean(x)), 'median':float(np.median(x)),'mode':float(min(an))}
    return ans