''' 
Truck Class
Write a class Truck that extends the class Vehicle. 
A truck has an instance variable of type boolean to define whether it has a trailer or not (default value: false). 
The method toString() of the class Truck prints the same message as the method of the class Vehicle, 
but it does also add another line with the content: has trailer: true/false, depending on the actual value.
'''
from Vehicle_Class import Vehicle

class Truck(Vehicle):
    def __init__(self, color,has_trailer:bool=False) -> None:
        super().__init__(color,)
        self.has_trailer = has_trailer
    
           
    def toString(self):
              return f"The vehicle is {self.getColor()}\nhas trailer:{self.has_trailer}"
if __name__ == '__main__':
    Truck1= Truck("red")
    print(Truck1.toString())