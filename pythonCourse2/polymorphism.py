class Car():
    def displacement(self):
        print("I moving use four whells")

class Motorcycle():
    def displacement(self):
        print("I moving use two whells")

class Truck():
    def displacement(self):
        print("I moving use eigth whells")

motorcycle1 = Motorcycle()
motorcycle1.displacement()
car1 = Car()
car1.displacement()
truck1 = Truck()
truck1.displacement()

print("----------Polymorphism--------------")

def vehicleDisplacement(vehicle):
    vehicle.displacement()

myVehicle = Truck()
vehicleDisplacement(myVehicle)
