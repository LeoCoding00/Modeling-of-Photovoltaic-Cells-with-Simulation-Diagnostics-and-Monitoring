#Celda, variable defin
from math import exp

class Celda():
    """Model of PV Cell
    default parameters:
    Voc ~ 0.7V
    Isc ~ 4A
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
        """Initialization of a photovoltaic cell, this element is characterized for outputting a voltage-current (I-V)
        characteristics for certain environmental conditions (so far only temperature and irradiance are considered)

        Args:
            enviro (Environment): Environment model that includes a temperature and irradiance conditions
        """
        self.enviro=enviro#receive an environment, with a Temperature T(Celsius) and an Irradiation G (W/m2) normal conditions are indicated by T_ref and G_ref
        self.T=self.enviro.temp+273.15#temperatures handled in Kelvin for the model
        self.calculate_parameters()#calculate all the parameters corresponding to each cell in the single diode model
        
    def calculate_parameters(self):
        """Calculate the real parameters directly after initializing the cell
        """
        self.Iph=self.photo_current()#photocurrent - Modeled as an independent voltage source, changes with irradiation
        self.I0=self.saturation_current()#saturation current, the reverse saturation current provided by the diode, few nA
        self.Vt=self.thermal_voltage()#thermal voltage in the diode, this corresponds to the voltage of the thermically excited electrons (kT/q)
        self.Voc=self.find_Voc()#Open circuit voltage, calculated directly
        self.Isc=self.find_current(0)#Short circuit current, using the already established find current method
    def photo_current(self):
        """Calculate the photocurrent (independent current source) of the single diode model

        Returns:
            int: Photocurrent (Iph) in A
        """
        return (Celda.Iph_ref*(self.enviro.irradiance/Celda.G_ref))#Photocurrent increases or diminishes based on the irradiation conditions compared to the reference environment
    
    def saturation_current(self):
        """Calculate the saturation current (diode reverse saturation current) of the single diode model
        
        Returns:
            int: Saturation current (I0) in A
        """
        return(Celda.I0_ref*((self.T/Celda.T_ref)**3)*exp(((Celda.q*Celda.Eg)/(Celda.n*Celda.k))*(1/Celda.T_ref-1/self.T)))
    
    def thermal_voltage(self):
        """Calculate the thermal voltage of the diode in the single diode model

        Returns:
            int: Thermal voltage (Vt=kT/q) in V
        """
        return (Celda.k*self.T/Celda.q)
    
    def find_bracket(self,V):
        """Calculate an upper- and lower-bounds for numerical solution of the current with
        the bisection method. 
        
        The current is going to be a value between 0A and the photocurrent (Iph) however, the
        bisection method requires one of the bounds to evaluate the numerical solution below 0 - f(V)<0 -
        and the other to evaluate it over zero - f(V)>0 - this does not always happen at the extreme bounds, so a good
        pair of limits must be found.

        Args:
            V (int): Voltage [V] at which the current is calculated

        Returns:
            tuple: A tuple with the limits and their evaluation, I_l and I_h can be both either of the limits
            but the function always returns a tuple of the form ((lower_bound,f(lower_bound),(upper_bound,f(upper_bound))))
        """
        I_h=0 #Extreme limit I=0A
        I_l=self.Iph#Extreme limit I=Photocurrent [A]
        f_h=self.equation(I_h,V)#Calculate f(I,V) for I_h and the indicated voltage 
        f_l=self.equation(I_l,V)#Calculate f(I,V) for I_l and the indicated voltage
        while(f_l*f_h)>=0:#calculate until one of the evaluations is positive and the other negative
            I_h=I_h+20e-3#Change guess, step-size=20mA
            I_l=I_l-20e-3#Change guess, step-size=20mA
            f_h=self.equation(I_h,V)#evaluate f(I_h,V) with the new guess
            f_l=self.equation(I_l,V)#evaluate f(I_l,V) with the new guess
        if (f_l>f_h):
            return ((I_h,f_h),(I_l,f_l))#Return of the form (lower_bound,upper_bound)
        else:
            return ((I_l,f_l),(I_h,I_l))#Return of the form (lower_bound,upper_bound)
        
    def equation(self,I,V):
        """Numerical evaluation of the I-V function, since an analytical solution is not feasible,
        the equation is rearranged of the form f(I,V)=0, for a given V, a current value (I) is guessed as a solution,
        if it is one solution f(I,V) will be zero.

        Args:
            I (int): guess solution of current in [A]
            V (int): voltage in [V] at which the cell is operating

        Returns:
            int: evaluation of the guessed current f(I,V)
        """
        return (self.Iph-self.I0*(exp((V+I*self.Rs)/(self.n*self.Vt))-1)
                -((V+I*self.Rs)/(self.Rsh))-I)
    def bisect(self,Ih,Il,V):
        """Bisection method. This is a numerical solution of the equation f(I,V), using two limits ()

        Args:
            Ih (int): Lower bound where f(I_h,V)<0
            Il (int): Upper bound where f(I_l,V)>0
            V (int): Operation voltage in [V]

        Returns:
            Im (int): Best guess solution for I in [A]
        """
        while(abs(Il-Ih)>1e-6):#A new guess is searched until there is a certainty guess of 1uA
            Im=(Il+Ih)/2#new guess
            fm=self.equation(Im,V)#evaluate f(I,V) for new guess
            if (fm>0):#updated the bounds accordingly
                Il=Im
            if (fm<0):
                Ih=Im
        return Im
    def find_current(self,V):
        """Find the current output of a cell for a given operation voltage

        Args:
            V (int): Operation voltage in [V]

        Returns:
            I (int): Solution current in [A]
        """
        (bracket_h,bracket_l)=self.find_bracket(V)#find bounds
        I=self.bisect(bracket_h[0],bracket_l[0],V)#apply numerical solution by bisection method
        return I
    
    def equation_Voc(self,Vk):
        """Find open circuit voltage (Voc) employing numerical methods and a simplified equation
        where I=0A (open circuit conditions)

        Args:
            Vk (int): Voc guess in [V]
            
        Returns:
            int: Solution of f(0,V) for the given guess
        """
        return(self.Iph-self.I0*(exp(Vk/(self.n*self.Vt))-1)
               - (Vk/self.Rsh))
    def derivative_Voc(self,Vk):
        """Find f'(0,V) for a given operation voltage, using the simplified equation for Voc

        Args:
            Vk (int): Voc guess in [V]
        """
        return(-self.I0*((1/(self.n*self.Vt))*exp(Vk/(self.n*self.Vt)))-(1/self.Rsh))
    def find_Voc(self,V_seed=0.7):
        """Find approximating Voc with a numerical solution, employing the Raphson-Newton Method.
        
        This method is redundant, as Voc can also be approximated with the find_voltage method,
        it is left here as legacy code

        Args:
            V_seed (float, optional): Seed to make the first guess of Voc. Defaults to 0.7.

        Returns:
            Voc (int): Best guess of Voc in [V]
        """
        Voc=V_seed-(self.equation_Voc(V_seed)/self.derivative_Voc(V_seed))#Raphson-Newton guess
        while(abs(Voc-V_seed)>1e-6):#Find a new solution until there is a certainty of 1uV
            V_seed=Voc
            Voc=V_seed-(self.equation_Voc(V_seed)/self.derivative_Voc(V_seed))
        return Voc
    def equation_v(self,I,Vk):
        """Find the I-V characteristics. In this case the full model is used and the voltage is
        guessed for a given current I
        
        Args:
            I (int): Operating current in [A]
            Vk (int): Seed to start guessing the voltage solution in [V]
            
        Returns:
            int: f(I,Vk) solution for the evaluation function
        
        """
        return(self.Iph-(Vk/self.Rsh)+(I*(self.Rs/self.Rsh-1))-(self.I0*(exp((Vk+I*self.Rs)/(self.n*self.Vt))-1)))
    def derivative_v(self,I,Vk):
        """Find f'(I,Vk) for a given current of operation.

        Args:
            I (int): Operation current in [A]
            Vk (int): Seed to start guessing the voltage in [V]

        Returns:
            int: solution for f'(I,V)
        """
        return ((-1/self.Rsh)-(self.I0*Vk*exp((Vk+self.Rs*I)/self.n*self.Vt)/(self.n*self.Vt)))
    def find_voltage(self,I,V_seed=0.7):
        """Approximate V numerically using the Raphson-Newton method

        Args:
            I (int): Operating current in [A]
            V_seed (float, optional): Seed to calculate the voltage solution in [V]. Defaults to 0.7.

        Returns:
            V(int): Approximate voltage of operation in [V] for a given current 
        """
        V=V_seed-(self.equation_v(I,V_seed)/self.derivative_v(I,V_seed))
        while (abs(V-V_seed)>1e-6):
            V_seed=V
            V=V_seed-(self.equation_v(I,V_seed)/self.derivative_v(I,V_seed))
        return V