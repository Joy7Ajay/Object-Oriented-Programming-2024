'''
Garage Class
Write a class Garage that has a Vehicle as an instance variable. 
This garage can be used by Cars and Trucks. Define a method setVehicle(Vehicle parked) to park a vehicle in the garage. 
Provide a method toString() to print a message Description of the parked vehicle 
... followed by the description of the vehicle that is in the garage at this moment.
'''
class Garage:
    def __init__(self):
        self.Vehicle = None
        

    def setVehicle(self, Vehicle_parked):
        self.Vehicle = Vehicle_parked
        return f"The car parked is {self.setVehicle}"
    
    def toString(self):
        return f"Description of the parked vehicle:\n {self.Vehicle.toString()}"
