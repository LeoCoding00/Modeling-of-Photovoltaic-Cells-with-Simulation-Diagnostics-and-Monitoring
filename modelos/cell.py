#Celda, variable defin
from math import exp

class Celda():
    """Model of PV Cell
    default parameters:
    Voc=0.7V
    Isc=4A
    Fill factor=0.87
    """
    #Environmental conditions
    G_ref=1000#W/m2 #reference irradiation for modeling of PC
    T_ref=25+273.15#C #reference temperature for modeling of I0 reverse saturation current
    
    #Reference cell parameters
    Iph_ref=4#A for normal conditions
    I0_ref=3e-9#A saturation current (leakage)
    
    #Physical parameters
    n=1.3#ideality factor 1=ideal
    Rs=0.01#Ohm, resistance of contacts, bulk, etc
    Rsh=1000#Ohm parallel, leakage
    area=0.01#m2
    
    #Physics
    q=1.6021e-19#Coulomb electron charge
    k=1.3806e-23#J/k boltzmann constant
    Eg=1.12#Si bandgap
    
    def __init__(self, enviro):
        self.enviro=enviro#receive a 
        self.T=self.enviro.temp+273.15
        self.calculate_parameters()
        
    def calculate_parameters(self):
        self.Iph=self.photo_current()
        self.I0=self.saturation_current()
        self.Vt=self.thermal_voltage()
        self.Voc=self.find_Voc()
        self.Isc=self.find_current(0)
    def photo_current(self):
        return (Celda.Iph_ref*(self.enviro.irradiance/Celda.G_ref))
    
    def saturation_current(self):
        return(Celda.I0_ref*((self.T/Celda.T_ref)**3)*exp(((Celda.q*Celda.Eg)/(Celda.n*Celda.k))*(1/Celda.T_ref-1/self.T)))
    
    def thermal_voltage(self):
        return (Celda.k*self.T/Celda.q)
    
    def find_bracket(self,V):
        I_h=0
        I_l=self.Iph
        f_h=self.equation(I_h,V)
        f_l=self.equation(I_l,V)
        while(f_l*f_h)>=0:
            I_h=I_h+20e-3
            I_l=I_l-20e-3
            f_h=self.equation(I_h,V)
            f_l=self.equation(I_l,V)
        if (f_l>f_h):
            return ((I_h,f_h),(I_l,f_l))
        else:
            return ((I_l,f_l),(I_h,I_l))
        
    def equation(self,I,V):
        return (self.Iph-self.I0*(exp((V+I*self.Rs)/(self.n*self.Vt))-1)
                -((V+I*self.Rs)/(self.Rsh))-I)
    def bisect(self,Ih,Il,V):
        #print("bisection")
        while(abs(Il-Ih)>1e-6):
            #print(f"Il={Il},Ih={Ih}")
            Im=(Il+Ih)/2
            #print(f"Im={Im}")
            fm=self.equation(Im,V)
            #print(f"f(Im)={fm}")
            if (fm>0):
                Il=Im
            if (fm<0):
                Ih=Im
        return Im
    def find_current(self,V):
        (bracket_h,bracket_l)=self.find_bracket(V)
        I=self.bisect(bracket_h[0],bracket_l[0],V)
        return I
    
    def equation_Voc(self,Vk):
        return(self.Iph-self.I0*(exp(Vk/(self.n*self.Vt))-1)
               - (Vk/self.Rsh))
    def derivative_Voc(self,Vk):
        return(-self.I0*((1/(self.n*self.Vt))*exp(Vk/(self.n*self.Vt)))-(1/self.Rsh))
    def find_Voc(self,V_seed=0.7):
        Voc=V_seed-(self.equation_Voc(V_seed)/self.derivative_Voc(V_seed))
        while(abs(Voc-V_seed)>1e-6):
            V_seed=Voc
            Voc=V_seed-(self.equation_Voc(V_seed)/self.derivative_Voc(V_seed))
        return Voc
    def equation_v(self,I,Vk):
        return(self.Iph-(Vk/self.Rsh)+(I*(self.Rs/self.Rsh-1))-(self.I0*(exp((Vk+I*self.Rs)/self.n*self.self.Vt)-1)))
    def derivative_v(self,I,Vk):
        return ((-1/self.Rsh)-(self.I0*Vk*exp((Vk+self.Rs*I)/self.n*self.Vt)/(self.n*self.Vt)))
    def find_voltage(self,I,V_seed=0.7):
        V=V_seed-(self.equation_v(I,V_seed)/self.derivative_v(I,V_seed))
        while (abs(V-V_seed)>1e-6):
            V_seed=V
            V=V_seed-(self.equation_v(I,V_seed)/self.derivative_v(I,V_seed))
        return V