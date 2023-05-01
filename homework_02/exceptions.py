"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
from dataclasses import dataclass

class Engine():
    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons

@dataclass
class Engine:
    volume: int
    pistons: int