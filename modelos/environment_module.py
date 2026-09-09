from modelos.environment import Environment
from numericals.stochastic_methods import stoch_disti as rdm_env

class EnvironmentMod(Environment):
    def __init__ (
        self,
        temperature=25,
        irradiance=1000,
        N=10,
        temp_std=0.5,
        irr_std=50,
    ):
        super().__init__(temperature,irradiance)
        self.N=N 
        self.temperatures=temperature+rdm_env(N,temp_std)
        self.irradiances=irradiance+rdm_env(N,irr_std)
        self.environments=[
            Environment(self.temperatures[i],self.irradiances[i])
            for i in range(self.N)]