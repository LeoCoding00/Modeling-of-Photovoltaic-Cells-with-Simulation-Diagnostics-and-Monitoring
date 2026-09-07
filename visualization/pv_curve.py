import numpy as np 
import matplotlib.pyplot as plt

def plot_pv(Voc,Is,voltages,currents):
    i=np.array(currents)
    v=np.array(voltages)
    p=i*v
    plt.figure(figsize=(12,8))
    plt.plot(v,p)
    plt.axhline(Is*Voc,color='red')
    plt.axvline(Voc,color='red')
    plt.title("P-V curve")
    plt.grid(True)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Power (W)")
    plt.show()