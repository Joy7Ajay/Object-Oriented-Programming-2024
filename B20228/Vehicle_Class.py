'''Vehicle Class
Write a class Vehicle. 
A Vehicle has an instance variable to store the color of the Vehicle. 
The color can be retrieved with the getColor() method. 
The toString() method returns a String like This vehicle is red, depending on the actual color.
'''

class Vehicle:
    def __init__(self,color):
        self.color = color
        
    def getColor(self):
        return self.color
        
    def toString(self):    
        print(f"This vehicle is {self.getColor()}")
        
a = Vehicle("red")
a.toString()
