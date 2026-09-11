from modelos.cell import Celda

class Module():
    """Adds a PV module composed of several cells with stochastic modeling.
    """
        
    def __init__(self,environments):
        """Declaration of a PV module

        Args:
            environments (EnvironmentMod): An environment model with N samples defines a PV module with N cells
        """
        self.environments=environments
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