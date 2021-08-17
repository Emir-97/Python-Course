class Car():
    def __init__(self):
        self.__chassisLength = 250
        self.__whells = 4
        self.__chassisWidth = 120
        self.__onGoing = False

    def tear(self, weStarted):
        self.__onGoing = weStarted

        if self.__onGoing:
            check = self.__internal_checkup()
        if (self.__onGoing and check):
            return "Car is on going"
        elif (self.__onGoing and check == False):
            return "Something has happened we can not start"
        else:
            return "The car is stopped"

    def status(self):
        print("Car has ", self.__whells, " whells. A width of ", self.__chassisWidth, " and a long of ",
             self.__chassisLength)

    def __internal_checkup(self):
        print("Performing internal check")
        self.gasoline = "ok"
        self.oil = "ok"
        self.doors = "ok"

        if(self.gasoline == "bad" and self.oil == "ok" and self.doors=="ok"):
            return True
        else:
            return False

myCar = Car()
print(myCar.tear(True))
myCar.status()

print("-------------------We are create the second object----------------------")

car2 = Car()

print(car2.tear(False))
car2.status()
