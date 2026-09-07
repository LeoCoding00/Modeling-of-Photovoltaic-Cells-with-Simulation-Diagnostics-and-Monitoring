import numpy as np 
import matplotlib.pyplot as plt

def plot_iv(Voc,Is,voltages,currents):
    i=np.array(currents)
    v=np.array(voltages)
    plt.figure(figsize=(12,8))
    plt.plot(v,i)
    plt.axhline(Is,color='red')
    plt.axvline(Voc,color='red')
    plt.title("I-V curve")
    plt.grid(True)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.show()