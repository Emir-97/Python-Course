class Vehicle():
    def __init__(self, model, trademark):
        self.model = model
        self.trademark = trademark
        self.onGoing = False
        self.accelerate = False
        self.brake = False

    def tear(self):
        self.onGoing = True

    def accelerates(self):
        self.accelerate = True

    def stop(self):
        self.brake = True

    def status(self):
        print("Trademark: ", self.trademark, "\nModel: ", self.model, "\nOn Going: ",
             self.onGoing, "\nSpeed up: ", self.accelerate, "\nBrake: ", self.brake)

class Motorcycle(Vehicle):
    wheellie1  = ""
    def wheellie(self):
        self.wheellie1 = "I am doing the wheelie"

        def status(self):
            print("Trademark: ", self.trademark, "\nModel: ", self.model, "\nOn Going: ",
                 self.onGoing, "\nSpeed up: ", self.accelerate, "\nBrake: ", self.brake,
                 "\n", self.wheellie1)

myMotorcycle = Motorcycle("ZR", "Yamaha")
myMotorcycle.status()
myMotorcycle.tear()
myMotorcycle.status()
