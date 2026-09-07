#environmental model

class Environment():
    """Environmental model
    temperature: Celsius, default 25
    irradiance: W/A, default 1000
    """
    def __init__(self,temp=25,irradiance=1000):
        self.temp=temp
        self.irradiance=irradiance
    