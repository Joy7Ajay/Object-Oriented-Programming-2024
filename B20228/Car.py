''' 
Car Class
Write a class Car that extends the class Vehicle. 
A car has an instance variable of type boolean to define whether it has winter tires or not (default value: false). 
The method toString() of the class Car prints the same message as the method of the class Vehicle, 
but it does also add another line with the content: has winter tires: true/false, depending on the actual value.
'''
from Vehicle_Class import Vehicle

class Car(Vehicle):
    def __init__(self,color,has_winter_tires:bool=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires
    def toString(self):
        return f"The vehicle is {self.getColor()}\nhas winter tires:{self.has_winter_tires}\n"
    
if __name__ == '__main__':
    car1 = Car("black")
    print(car1.toString())