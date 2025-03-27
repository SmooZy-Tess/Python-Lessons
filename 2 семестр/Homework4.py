print("------------- Number 3 -------------")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, name):
        return "This attribute is not available"


c = Car("Toyota", "Corolla")
print(c.make)      
print(c.model)     
print(c.color)   
  
print("------------- Number 4 -------------")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name not in ['width', 'height']:
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(name, value)


try:
    r = Rectangle(10, 20)
    r.width = 15  
    r.height = 25 
    r.color = 'red'  
except AttributeError as e:
    print(e)

    
