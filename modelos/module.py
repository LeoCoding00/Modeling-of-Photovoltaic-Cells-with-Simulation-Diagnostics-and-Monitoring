from modelos.cell import Celda
import numpy as np 

class Module():
    """Adds a PV module composed of several cells with stochastic modeling.
    """
        
    def __init__(self,environments_m):
        """Declaration of a PV module

        Args:
            environments (EnvironmentMod): An environment model with N samples defines a PV module with N cells
        """
        self.environments=environments_m.environments
        self.celdas=[]
        self.add_cells()#creates and adds all cells in the list celdas
        self.Isc=self.calc_Isc()#Isc of the module
        self.Voc=self.calc_Voc()#Voc of the module
    def add_cells(self):
        """Add a cell for each sample of the environment module. They are saved in the list celdas
        """
        for evn in self.environments:
            self.celdas.append(Celda(evn))
    def calc_Isc(self):
        """Finds the Short Circuit current (Isc) of the entire module. Isc of the module
        is limited by the smallest Isc in the cell array.

        Returns:
            Isc (int): Short Circuit current of the module in [A]
        """
        Isc=255#Start with a high current for comparison purposes
        for celda in self.celdas:#go over every single cell
            if (celda.Isc<Isc):
                Isc=celda.Isc
        return Isc
    def calc_Voc(self):
        """Calculated the Open Circuit Voltage (Voc) of the entire PV module. Voc of the module
        is the series equivalent of all the Voc of each single cell, mathematically calculated as the addition
        of all the individual Voc

        Returns:
            Voc (int): Voc of the entire module
        """
        Voc=0
        for celda in self.celdas:
            Voc=Voc+celda.Voc
        return Voc
    def find_voltage(self,I):
        """Approximate the operation voltage of the entire module by adding, in series,
        the voltage of each cell of the module

        Args:
            I (int): Operation current in [A]
            
        Returns:
            V (int): The approximate voltage in [V] for the given operation current
        """
        
        V=0
        for celda in self.celdas:
            V_cell=celda.find_voltage(I,V_seed=celda.Voc)
            V=V+V_cell
        return V
    
    def find_characteristics(self,step=0.001):
        """Approximates the I-V and P-V characteristics of the module. The characteristics are calculated
        between 0 and the short circuit current of the module

        Args:
            step (float, optional): Describes the granularity of the numerical simulation, the step
            size between two consecutive points in I-V and P-V curves. Defaults to 0.001, which represents 1mA.
            
        Returns:
            (voltage,current,power) (tuple, float): A tuple with three positions
            First is voltage in [V]
            second is current in [A]
            third is power in [W]
        """
        I=np.arange(0,self.Isc,step)
        V=np.array([self.find_voltage(i_point) for i_point in I])
        P=I*V
        
        return (V,I,P)