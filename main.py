#PV Monitoring v1.0
#Practice in photovoltaic
#Author: Joel Leandro Gomez Quintero
import datetime
from modelos.environment import Environment as evn
from modelos.cell import Celda
from modelos.environment_module import EnvironmentMod as evn_m
from modelos.module import Module as PV_Module
from visualization import iv_curve,pv_curve

def main():
    print('PV Monitoring mock-up project v1.0')
    print('Author Joel Leandro Gomez Quintero')
    print(datetime.date.today())
    print("Environment 1")
    env1=evn_m(27,1200)
    print(f"Nominal values:\nT={env1.temp}C\nG={env1.irradiance}W/m2")
    print("Module 1")
    modulo1=PV_Module(env1)
    print(f"Module 1:\nIsc={modulo1.Isc:.3f}A\nVoc={modulo1.Voc:.2f}V")
    (voltages,currents,powers)=modulo1.find_characteristics()
    print(voltages)
    print(currents)
    print(powers)
    
    
        
    
if __name__=="__main__":
    main()