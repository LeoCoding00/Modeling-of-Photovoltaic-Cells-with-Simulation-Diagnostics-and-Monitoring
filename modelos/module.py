from modelos.cell import Celda

class Module():
        
    def __init__(self,environments):
        self.environments=environments
        self.celdas=[]
        self.add_cells()
        self.Isc=self.calc_Isc()
        self.Voc=self.calc_Voc()
    def add_cells(self):
        for evn in self.environments:
            self.celdas.append(Celda(evn))
    def calc_Isc(self):
        Isc=999
        for celda in self.celdas:
            if (celda.Isc<Isc):
                Isc=celda.Isc
        return Isc
    def calc_Voc(self):
        Voc=0
        for celda in self.celdas:
            Voc=Voc+celda.Voc
        return Voc