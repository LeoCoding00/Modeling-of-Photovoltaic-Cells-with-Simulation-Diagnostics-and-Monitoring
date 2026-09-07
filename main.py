#PV Monitoring v1.0
#Practice in photovoltaic
#Author: Joel Leandro Gomez Quintero
import datetime
from modelos import cell,environment
from visualization import iv_curve,pv_curve

def main():
    print('PV Monitoring mock-up project v1.0')
    print('Author Joel Leandro Gomez Quintero')
    print(datetime.date.today())
    print("Si cell 1")
    env1=environment.Environment(26,500)
    celda1=cell.Celda(enviro=env1)
    print(f"Temperature:{celda1.enviro.temp}C")
    print(f"Irradiance:{celda1.enviro.irradiance}W/m2")
    print(f"Photocurrent:{celda1.Iph}A")
    print(f"Saturation current:{celda1.I0}A")
    print(f"Thermal voltage:{celda1.Vt}V")
    print(f"Series resistance:{celda1.Rs}Ohm")
    print(f"Shunt resistance:{celda1.Rsh}")
    print(f"Ideality factor:{celda1.n}")
    
    print("Physics model:")
    print(f"Voc={celda1.Voc}")
    print(f"Isc={celda1.Isc}")
    c1_voltages=[]
    c1_currents=[]
    for i in range(1,101):
        c1_voltages.append(celda1.Voc*i/100)
        c1_currents.append(celda1.find_current(celda1.Voc*i/100))
    iv_curve.plot_iv(celda1.Voc,celda1.Isc,c1_voltages,c1_currents)
    pv_curve.plot_pv(celda1.Voc,celda1.Isc,c1_voltages,c1_currents)
        
    
    print("Si cell 2")
    env2=environment.Environment(temp=25,irradiance=1000)
    celda2=cell.Celda(env2)
    print(f"Temperature:{celda2.enviro.temp}C")
    print(f"Irradiance:{celda2.enviro.irradiance}W/m2")
    print(f"Photocurrent:{celda2.Iph}A")
    print(f"Saturation current:{celda2.I0}A")
    print(f"Thermal voltage:{celda2.Vt}V")
    print(f"Series resistance:{celda2.Rs}Ohm")
    print(f"Shunt resistance:{celda2.Rsh}Ohm")
    print(f"Ideality factor:{celda2.n}")
    print("Physics model:")
    print(f"Voc={celda2.Voc}")
    print(f"Isc={celda2.Isc}")
    c2_voltages=[]
    c2_currents=[]
    for i in range(1,101):
        c2_voltages.append(celda2.Voc*i/100)
        c2_currents.append(celda2.find_current(celda2.Voc*i/100))
    iv_curve.plot_iv(celda2.Voc,celda2.Isc,c2_voltages,c2_currents)  
    pv_curve.plot_pv(celda2.Voc,celda2.Isc,c2_voltages,c2_currents)
    print("sup")  
    
    
if __name__=="__main__":
    main()