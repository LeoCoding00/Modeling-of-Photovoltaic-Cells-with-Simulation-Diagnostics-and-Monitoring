#PV Monitoring v1.0
#Practice in photovoltaic
#Author: Joel Leandro Gomez Quintero
import datetime
from modelos.environment import Environment as evn
from modelos.cell import Celda
from modelos.environment_module import EnvironmentMod as evn_m
from visualization import iv_curve,pv_curve

def main():
    print('PV Monitoring mock-up project v1.0')
    print('Author Joel Leandro Gomez Quintero')
    print(datetime.date.today())
    print("Environment 1")
    env1=evn(25,100)
    print(f"Nominal values:\nT={env1.temp}C\nG={env1.irradiance}W/m2")
    string1=evn_m()
    print(string1.temperatures)
    print(string1.irradiances)
    print("Environment 2")
    env2=evn(19,500)
    print(f"Nominal values:\nT={env2.temp}C\nG={env2.irradiance}W/m2")
    string2=evn_m(temperature=env2.temp,irradiance=env2.irradiance,N=20)
    print(string2.temperatures)
    print(string2.irradiances)
    # celda1=cell.Celda(enviro=env1)
    # print(f"Temperature:{celda1.enviro.temp}C")
    # print(f"Irradiance:{celda1.enviro.irradiance}W/m2")
    # print(f"Photocurrent:{celda1.Iph}A")
    # print(f"Saturation current:{celda1.I0}A")
    # print(f"Thermal voltage:{celda1.Vt}V")
    # print(f"Series resistance:{celda1.Rs}Ohm")
    # print(f"Shunt resistance:{celda1.Rsh}")
    # print(f"Ideality factor:{celda1.n}")
    
    # print("Physics model:")
    # print(f"Voc={celda1.Voc:.3f}")
    # print(f"Isc={celda1.Isc:.3f}")
    # c1_voltages=[]
    # c1_currents=[]
    # for i in range(1,101):
    #     c1_voltages.append(celda1.Voc*i/100)
    #     c1_currents.append(celda1.find_current(celda1.Voc*i/100))
    # c1_power=[V*I for V,I in zip(c1_voltages,c1_currents)]
    # Pmax=max(c1_power)
    # mpp=c1_power.index(Pmax)
    # Vmax=c1_voltages[mpp]
    # Imax=c1_currents[mpp]
    # print(f"Maximum Power MPP:\n{Vmax:.3f}V\n{Imax:.3f}A\n{Pmax:.3f}W")
    # print(f"FF={Pmax/(celda1.Voc*celda1.Isc):.3f}\nEfficiency={Pmax/(celda1.area*celda1.enviro.irradiance):.3f}")
    
    # iv_curve.plot_iv(celda1.Voc,celda1.Isc,c1_voltages,c1_currents)
    # pv_curve.plot_pv(celda1.Voc,celda1.Isc,c1_voltages,c1_currents)
        
    
    # print("Si cell 2")
    # env2=environment.Environment(temp=25,irradiance=1000)
    # celda2=cell.Celda(env2)
    # print(f"Temperature:{celda2.enviro.temp}C")
    # print(f"Irradiance:{celda2.enviro.irradiance}W/m2")
    # print(f"Photocurrent:{celda2.Iph}A")
    # print(f"Saturation current:{celda2.I0}A")
    # print(f"Thermal voltage:{celda2.Vt}V")
    # print(f"Series resistance:{celda2.Rs}Ohm")
    # print(f"Shunt resistance:{celda2.Rsh}Ohm")
    # print(f"Ideality factor:{celda2.n}")
    # print("Physics model:")
    # print(f"Voc={celda2.Voc}")
    # print(f"Isc={celda2.Isc}")
    # c2_voltages=[]
    # c2_currents=[]
    # c2_power=[]
    # for i in range(1,101):
    #     c2_voltages.append(celda2.Voc*i/100)
    #     c2_currents.append(celda2.find_current(celda2.Voc*i/100))
    # iv_curve.plot_iv(celda2.Voc,celda2.Isc,c2_voltages,c2_currents)  
    # pv_curve.plot_pv(celda2.Voc,celda2.Isc,c2_voltages,c2_currents)
        
    
if __name__=="__main__":
    main()