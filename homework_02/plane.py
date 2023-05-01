"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption, max_cargo):
        super().__init__(self, weight, started, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, load_cargo):
        if load_cargo + self.cargo <= self.max_cargo:
            self.cargo += load_cargo
        else:
            raise CargoOverload('CargoOverload')

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before


