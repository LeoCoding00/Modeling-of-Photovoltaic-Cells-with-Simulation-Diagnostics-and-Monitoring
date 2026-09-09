import numpy as np 

def stoch_disti(N,std,mean=0):
    return np.random.normal(mean,std,N)