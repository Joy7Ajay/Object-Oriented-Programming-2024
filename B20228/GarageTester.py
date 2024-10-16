'''
GarageTester Class
Write a class GarageTester with a method getExample() (see template). 
In this method, create an object of the Truck class (color is black, and the truck has no trailer). 
Create an object of the Garage class. 
Put the Truck into the Garage.

'''

from Garage import Garage
from Truck import Truck


class GarageTester(Garage):
    def __init__(self):
        super().__init__()

    def getExample(self):
        truck = Truck('black', False)
        my_garage = Garage()
        my_garage.setVehicle(truck)
        return my_garage.toString()


if __name__ == '__main__':
    print(GarageTester().getExample())

	
 