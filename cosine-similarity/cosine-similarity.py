import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    am=np.linalg.norm(a)
    bm=np.linalg.norm(b)
    if am==0 or bm ==0:
        return 0.0
    return float(np.dot(a,b)/(am*bm))