from modelos.environment import Environment
from numericals.stochastic_methods import stoch_disti as rdm_env

class EnvironmentMod(Environment):
    """_summary_

    Args:
        Environment (Environment): Parent class Environment, representing nominal T and G
    """
    def __init__ (
        self,
        temperature=25,#temperature in celcius
        irradiance=1000,#irradiance in W/m2
        N=10,#number of cells per module
        temp_std=0.1,#standard deviation of temperature
        irr_std=10,#standard deviation of irradiance
    ):
        """Initializing environment

        Args:
            temperature (int, optional): Nominal value of the temperature of the module. Defaults to 25.
            irradiance (int,optional): Nominal value of the irradiation of the module. Defaults to 1000.
            N (int,optional): Number of cells in a single module. Defaults to 10.
            temp_std (float, optional): Standard deviation of the distribution of temperature in the module. Defaults to 0.1C.
            irr_std (float,optional): Standard deviation of the distribution of irradiation in the module. Defaults to 10W/m2.
        """
        super().__init__(temperature,irradiance)
        self.N=N 
        self.temperatures=self.temp+rdm_env(N,temp_std)
        self.irradiances=self.irradiance+rdm_env(N,irr_std)
        self.environments=[
            Environment(self.temperatures[i],self.irradiances[i])
            for i in range(self.N)]