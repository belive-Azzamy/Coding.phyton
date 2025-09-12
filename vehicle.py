#Multiple inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Brand : {self.brand}, Model : {self.model}")
    
class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_battery(self):
        print(f"Battery capacity : {self.battery_capacity} kwh")

class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, model, battery_capacity, range_per_charge):
        Vehicle.__init__(self, brand, model)
        Electric.__init__(self, battery_capacity)
        self.range_per_charge = range_per_charge

    def info(self):
        Vehicle.info(self)
        print(f"Range per Charge {self.range_per_charge} km")

tesla = ElectricCar("Tesla", "Model 3", 100, 300)
tesla.info()
tesla.display_battery()