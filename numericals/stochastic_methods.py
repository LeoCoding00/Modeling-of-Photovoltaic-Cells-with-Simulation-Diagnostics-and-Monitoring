import numpy as np 

def stoch_disti(N,std,mean=0):
    """Local function for the generation of normal distributions of N samples and a given standard deviation.
    

    Args:
        N (int): Number of samples in the distribution
        std (float): Standard deviation of the distribution
        mean (int, optional): _description_. Defaults to 0.

    Returns:
        ndarray: An array with N samples that follow a normal distribution centered in mean
    """
    return np.random.normal(mean,std,N)